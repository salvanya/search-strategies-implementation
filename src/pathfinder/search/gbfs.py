from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node
# from math import sqrt


def heuristic(node_state, end, weight):
            x1, y1 = node_state
            x2, y2 = end
            return (abs(x2 - x1) + abs(y2 - y1) + weight)
            
class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """

        # Initialize a node with the initial position
        
        node = Node("", grid.start, heuristic(grid.start, grid.end, grid.get_cost(grid.start)))

        # Initialize the frointier
        frontier = PriorityQueueFrontier()

        # Add the root to the frontier
        frontier.add(node, node.cost)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Add the node to the explored dictionary
        explored[node.state] = node
        
        while True:
            # Fail if the froiner is empty
            if frontier.is_empty():
                return NoSolution(explored)
            
            # Pop a node from the frontier
            node = frontier.pop()

            # If the node is the goal, return the solution
            if node.state == grid.end:
                return Solution(node, explored)

            # Add neightbours to frontier 
            neightbours = grid.get_neighbours(node.state)
            
            for neightbour in neightbours:
                new_state = neightbours[neightbour]
                new_cost = heuristic(node.state, grid.end, grid.get_cost(new_state))

                if new_state not in explored or new_cost < explored[new_state].cost:
                    new_node = Node("", new_state, new_cost)
                    new_node.parent = node
                    new_node.action = neightbour

                    # Add the node to explored
                    explored[new_node.state] = new_node

                    #Add the node to frontier
                    frontier.add(new_node, new_node.cost)

