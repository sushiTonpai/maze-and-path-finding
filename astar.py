import heapq
from dataclasses import dataclass
from random import random

from constants import COLS, ROWS
from maze import Maze
from node import Node, get_start_end


@dataclass
class Astar:
    node_grid: list[list[Node]]
    start_node: Node
    goal_node: Node

    @classmethod
    def node_init(cls, maze_grid):
        """
         Initialize the A* object with nodes from a maze grid, setting start and goal nodes.
        """
        nodes = [[Node.cell_to_node(cell) for cell in row] for row in maze_grid]

        start_node, goal_node = get_start_end(nodes)
        start_node.g_cost = 0
        start_node.h_cost = start_node.estimate_cost(target=goal_node)
        start_node.f_cost = start_node.calculate_cost()

        return cls(node_grid=nodes,
                   start_node=start_node,
                   goal_node=goal_node, )

    def find_path(self) -> list[Node]:
        """
        Perform the A* search algorithm to find the path from start to goal nodes.
        """
        open_list = []
        searched_list = set()
        # Start the search from the starting node, open_list is a priority queue
        heapq.heappush(open_list, self.start_node)
        while len(open_list) > 0:
            current_node = heapq.heappop(open_list)
            searched_list.add(current_node)

            # If the goal is reached, return the constructed path
            self.check_goal_reached(current_node)

            neighbours = self.walkable_neighbours(current_node=current_node)

            def update_neighbour(current: Node, neighbour: Node, g_cost: float) -> None:
                neighbour.g_cost = g_cost
                neighbour.h_cost = neighbour.estimate_cost(target=self.goal_node)
                neighbour.f_cost = neighbour.calculate_cost()
                neighbour.parent = current
                # Add neighbour to open_list if not already present
                if neighbour not in open_list:
                    heapq.heappush(open_list, neighbour)

            for neighbour in neighbours:
                # Skip neighbours that have already been processed
                if neighbour in searched_list:
                    continue

                else:
                    new_g = current_node.g_cost + 1
                    # Update the neighbour's cost if the new cost is lower or if it's not in open_list
                    if new_g < neighbour.g_cost or neighbour not in open_list:
                        update_neighbour(current_node, neighbour, new_g)

        # return empty list if function cannot reach goal node
        return []

    def walkable_neighbours(self, current_node: Node) -> list[Node]:
        """
        Get the walkable neighbours of the given node in the maze.
        """
        neighbours = []
        # 4 direction [(west)(east)(north)(south)]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbour_x, neighbour_y = current_node.node_x + dx, current_node.node_y + dy
            if 0 <= neighbour_x < COLS and 0 <= neighbour_y < ROWS:  # out of bound check
                if not self.node_grid[neighbour_x][neighbour_y].is_wall:  # not a wall check
                    neighbours.append(self.node_grid[neighbour_x][neighbour_y])
        # print(neighbours)
        return neighbours

    def get_path(self) -> list[Node]:
        """
        Reconstruct the path from the goal node to the start node.
        Returns: list[Node]
        """
        path = []
        current_node = self.goal_node

        while current_node != self.start_node:
            path.insert(0, current_node)
            current_node = current_node.parent
        return path

    def check_goal_reached(self, current_node: Node) -> list[Node]:
        if current_node == self.goal_node:
            return self.get_path()
        return []


if __name__ == "__main__":
    # Generate a test maze
    test_maze = Maze.maze_generator()

    # Initialize A* with nodes from the maze
    test_nodes = Astar.node_init(maze_grid=test_maze)

    # Perform the A* search and print the resulting path
    path = Astar.find_path(test_nodes)
    print("Path:", path)
