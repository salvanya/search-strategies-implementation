from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Initialize the frontier with the inital node
        frontier = StackFrontier()
        frontier.add(node)

        while True:
            # Fail if the froiner is empty
            if frontier.is_empty():
                return NoSolution(explored)
            
            # Remove a node from the frontier
            node = frontier.remove()

            #Check if the node was already explored
            
            # Mark the node as explored
            explored[node.state] = True

            # If the node is the goal, return the solution
            if node.state == grid.end:
                return Solution(node, explored)

            #
            neightbours = grid.get_neighbours(node.state)
            for neightbour in neightbours:
                new_state = neightbours[neightbour]
                if new_state not in explored:
                    new_node = Node("", new_state, grid.get_cost(new_state))
                    new_node.parent = node
                    new_node.action = neightbour
                    frontier.add(new_node)






