import random
import pygame, sys

#note:

class Grid:
    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[0] * self.columns for _ in range(self.rows)]

    def draw(self, window):
        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.cells[row][column]
                color = (0, 255, 0) if cell else (55, 55, 55)
                pygame.draw.rect(window, color, 
                                    (column * self.cell_size, row * self.cell_size, 
                                    self.cell_size - 1, self.cell_size - 1))

    def fill_random(self):
        self.cells = [[random.choice([1, 0, 0, 0]) for _ in range(self.columns)] for _ in range(self.rows)]

    def clear(self):
        self.cells = [[0] * self.columns for _ in range(self.rows)]

    def toggle_cell(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            # Bitwise XOR to toggle between 0 and 1
            self.cells[row][column] ^= 1


class Simulation:
    NEIGHBOR_OFFSETS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.temp_grid = Grid(width, height, cell_size)
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.run = False

    def draw(self, window):
        self.grid.draw(window)

    def count_live_neighbors(self, row, column):
        live_neighbors = 0
        for offset in self.NEIGHBOR_OFFSETS:
            new_row = (row + offset[0]) % self.rows
            new_column = (column + offset[1]) % self.columns
            if self.grid.cells[new_row][new_column] == 1:
                live_neighbors += 1
        return live_neighbors

    def update(self):
        if not self.is_running():
            return

        for row in range(self.rows):
            for column in range(self.columns):
                live_neighbors = self.count_live_neighbors(row, column)
                cell_value = self.grid.cells[row][column]

                if cell_value == 1:
                    # Live cells die without neighbors
                    self.temp_grid.cells[row][column] = 1 if 2 <= live_neighbors <= 3 else 0
                else:
                    # Dead cells come to life if they have exactly 3 neighbors
                    self.temp_grid.cells[row][column] = 1 if live_neighbors == 3 else 0

        self.grid, self.temp_grid = self.temp_grid, self.grid

    def stop(self):
        self.run = False

    def clear(self):
        if not self.is_running():
            self.grid.clear()

    def create_random_state(self):
        if not self.is_running():
            self.grid.fill_random()

    def is_running(self):
        return self.run

    def start(self):
        self.run = True

    def toggle_cell(self, row, column):
        if not self.is_running():
            self.grid.toggle_cell(row, column)


pygame.init()

GREY = (42, 42, 42)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
CELL_SIZE = 10
FPS = 10

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

clock = pygame.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                simulation.create_random_state()
                simulation.start()
                pygame.display.set_caption("Game of Life - In Progress")
            elif event.key == pygame.K_SPACE:
                simulation.stop()
                pygame.display.set_caption("Game of Life - Simulation Stopped")
            elif event.key == pygame.K_r:
                simulation.create_random_state()
            elif event.key == pygame.K_c:
                simulation.clear()

                
    simulation.update()
    window.fill(GREY)
    simulation.draw(window)

    pygame.display.update()
    clock.tick(FPS)