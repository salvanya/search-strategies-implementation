# Interactive Pathfinding Visualizer

A Pygame-based application that demonstrates the step-by-step execution of uninformed and informed search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Uniform Cost Search (UCS)
- Greedy Best-First Search (GBFS)
- A* Search

This project is designed for educational purposes, offering a visual and interactive way to understand pathfinding algorithms. It also serves as a base for those interested in implementing their own algorithms.

## Key Features

- **Maze Creation**: Create mazes manually by placing and removing walls or generate them automatically using algorithms like:
  - Recursive Division
  - Prim's Algorithm
  - Randomized Depth-First Search
  - Basic Random Maze
  - Weighted Random Maze
- **Animation Control**: Adjust the speed of the pathfinding animations.
- **Algorithm Comparison**: Run multiple algorithms on the same or different mazes simultaneously, and view a comparative summary of:
  - Steps explored
  - Path length
  - Path cost
  - Time taken

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/salvanya/search-strategies-implementation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd pygame_pathfinding
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python run.pyw
   ```

## How to Use

- **Placing Walls**: Click on an empty cell to place a wall.
- **Removing Walls**: Click on a wall to remove it.
- **Adding Weights**: Hold down a number key (representing the weight) and click on a cell to assign a weighted cost to the path.
- **Setting Start and End Points**:
  - Click and drag the arrow to set the start point.
  - Click and drag the target to set the end point.
- **Testing Custom Algorithms**: To test your own implementations, modify the algorithm files located in `src/pathfinder/search/`.

### Directory Structure

```
src/pathfinder/search
|-- astar.py
|-- bfs.py
|-- dfs.py
|-- gbfs.py
|-- goright.py
|-- ucs.py
```
Each file corresponds to an individual search algorithm. You can customize or replace the existing implementations.

## Visual Example

Below is an example of the A* algorithm solving a maze generated automatically:

![A* Example](astar_example.gif)

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Motivation

This project was created to provide a visual and interactive way to learn uninformed and informed search algorithms. It is ideal for:

- Students studying search algorithms.
- Developers looking to experiment with or extend pathfinding implementations.

Contributions and feedback are welcome!

## Thanks
This repository uses code written by Mauro Lucci: https://github.com/maurolucci/tuia-prog3.git
