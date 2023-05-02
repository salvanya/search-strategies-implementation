from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Mark the node as explored
        explored[node.state] = True

        # Check if first node (root) is solution
        # Return if the node contains a goal state
        if node.state == grid.end:
            return Solution(node, explored)
        
        # Initialize the frontier with the initial node
        frontier = QueueFrontier()
        frontier.add(node)

        while True:

            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(explored)

            # Remove a node from the frontier
            node = frontier.remove()

            neighbours = grid.get_neighbours(node.state)
            for possible_action in neighbours:
                new_state = neighbours[possible_action]
                child_node = Node("", new_state , node.cost + grid.get_cost(new_state))
                child_node.parent = node
                child_node.action = possible_action

                # Return if the node contains a goal state
                if child_node.state == grid.end:
                    return Solution(node, explored)
                
                if child_node.state not in explored:
                    # Add the node to the explored dictionary
                    explored[child_node.state] = True
                    # Add the new node to the frontier
                    frontier.add(child_node)
