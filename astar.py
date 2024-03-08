import heapq
from dataclasses import dataclass

from constants import COLS, ROWS
from node import Node


@dataclass
class Astar:
    node_grid: list[list[Node]]
    start_node: Node
    goal_node: Node
    open_list: list[Node]
    searched_list: list[Node]

    @classmethod
    def node_init(cls, maze_grid, start_node, goal_node):
        nodes = [[Node.cell_to_node(cell) for cell in row] for row in maze_grid]
        return cls(node_grid=nodes,
                   start_node=start_node,
                   goal_node=goal_node,
                   open_list=[],
                   searched_list=[])

    def find_path(self) -> list[Node]:
        """
        return list of Nodes from start to goal
        """
        # start the search from the starting node, search list is priority Q
        heapq.heappush(self.open_list, self.start_node)
        while len(self.open_list) > 0:
            current_node = heapq.heappop(self.open_list)
            self.searched_list.append(current_node)

            if current_node == self.goal_node:
                return self.get_path()

            neighbours = self.walkable_neighbours(current_node=current_node)
            for neighbour in neighbours:
                new_g = current_node.g_cost + 1
                if new_g < neighbour.g_cost and current_node not in self.open_list:
                    neighbour.g_cost = new_g
                    neighbour.h_cost = neighbour.estimate_cost(target=self.goal_node)
                    neighbour.f_cost = neighbour.calculate_cost()
                    neighbour.parent = current_node
                if current_node not in self.open_list:
                    heapq.heappush(self.open_list, neighbour)

        # return empty list if function cannot reach goal node
        return []

    def walkable_neighbours(self, current_node: Node) -> list[Node]:
        neighbours = []
        # 4 direction [(west)(east)(north)(south)]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbour_x, neighbour_y = current_node.node_x + dx, current_node.node_y + dy
            if 0 <= neighbour_x < COLS and 0 <= neighbour_y < ROWS:  # out of bound check
                if not current_node.is_wall:  # not a wall check
                    neighbours.append(self.node_grid[neighbour_x][neighbour_y])
        return neighbours

    def get_path(self) -> list[Node]:
        """
        construct path from start to goal
        Returns: list[Node]
        """
        path = []
        current_node = self.goal_node

        while current_node != self.start_node:
            path.insert(0, current_node)
            current_node = current_node.parent
        return path
