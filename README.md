Here's a README file in Markdown format for your implementation of Conway's Game of Life:

---

# Conway's Game of Life

This is a Python implementation of Conway's Game of Life using the `pygame` library. The Game of Life is a cellular automaton devised by mathematician John Horton Conway. The simulation consists of a grid of cells, where each cell can be alive or dead. The state of each cell changes based on the number of live neighbors it has, following a set of simple rules.

## Features

- **Interactive Simulation:** Start, stop, clear, and randomize the grid using keyboard controls.
- **Grid Customization:** Adjustable grid size and cell size.
- **Real-time Visualization:** Observe the evolution of the grid in real-time.

## Installation

1. Ensure you have Python installed on your system (version 3.6 or later).
2. Install the `pygame` library if you haven't already:

   ```bash
   pip install pygame
   ```

3. Clone or download this repository to your local machine.

## Usage

1. Run the simulation using the following command:

   ```bash
   python game_of_life.py
   ```

2. The simulation window will open, displaying the grid. You can control the simulation using the following keys:

   - **`Enter`**: Start the simulation with a random initial state.
   - **`Space`**: Stop the simulation.
   - **`R`**: Randomize the grid while the simulation is stopped.
   - **`C`**: Clear the grid while the simulation is stopped.

3. Close the simulation by clicking the window's close button or using your system's method to terminate the process.

## Configuration

You can customize the simulation parameters by modifying the following variables in the script:

- `WINDOW_WIDTH` and `WINDOW_HEIGHT`: Set the dimensions of the simulation window.
- `CELL_SIZE`: Define the size of each cell in the grid.
- `FPS`: Adjust the frames per second, which controls the simulation speed.

## How It Works

- **Grid and Cells:** The simulation grid is represented by a 2D array where each cell can be alive (1) or dead (0).
- **Simulation Rules:** The state of each cell in the grid is updated every frame based on the number of live neighbors:
  - A live cell with fewer than two live neighbors dies (underpopulation).
  - A live cell with two or three live neighbors continues to live.
  - A live cell with more than three live neighbors dies (overpopulation).
  - A dead cell with exactly three live neighbors becomes alive (reproduction).
- **Grid Updates:** The grid updates are performed in a temporary grid to avoid conflicts during the state transition, and then the grids are swapped.

## Acknowledgments

This implementation is based on the classic rules of Conway's Game of Life. The `pygame` library is used for real-time visualization and interaction. Based on Python-Game-Of-Life-with-Pygame by [@educ8s](https://github.com/educ8s/Python-Game-Of-Life-with-Pygame/tree/main) with some changes in implementation.

## License

MIT License.

---
