from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the frontier with the inital node
        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost)

        # Initialize the explored dictionary to be empty
        explored = {node.state: node} 
        
        while True:
            # Fail if the froiner is empty
            if frontier.is_empty():
                return NoSolution(explored)
            
            # Pop a node from the frontier
            node = frontier.pop()

            # If the node is the goal, return the solution
            if node.state == grid.end:
                return Solution(node, explored)

            # Add unexplored neightbours to frontier
            neightbours = grid.get_neighbours(node.state)
            for neightbour in neightbours:
                new_state = neightbours[neightbour]
                new_cost = node.cost + grid.get_cost(new_state)
                
                if new_state not in explored or new_cost < explored[new_state].cost:
                    new_node = Node("", new_state, new_cost)
                    new_node.parent = node
                    new_node.action = neightbour
                               
                    # Mark the node as explored
                    explored[new_node.state] = new_node
                    frontier.add(new_node, new_node.cost)

