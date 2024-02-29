from __future__ import annotations
from dataclasses import dataclass

from cell import Cell, MazeType


@dataclass
class Node:
    """
    A* algorithm F(n) = G(n) + H(n) where n is Cell
    F(n) represents the total cost of that node
    G(n) represents the distance to that node from the starting node
    H(n) represents the estimate distance to goal
    H(n) distance calculate by manhattan distance -> abs(current.x - goal.x) + abs(current.y - goal.y)

    """
    g_cost: int
    h_cost: int
    parents: Cell
    start: Cell
    goal: Cell

    def f_cost(self):
        return self.g_cost + self.h_cost

    @classmethod
    def get_distance(cls) -> int:  # distance from current node to neighbour node
        return 1

    def cost_to_node(self, neighbour: Node) -> int:  # calculate G(n) cost
        return self.g_cost + neighbour.get_distance()


def walkable_path(cell, maze) -> list[Cell] or bool:
    neighbours = []
    # 4 direction [(west)(east)(north)(south)]
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        cell_neighbour = cell.x + dx, cell.y + dy
        if 0 <= cell_neighbour[0] < len(maze[0]) and 0 <= cell_neighbour[1] < len(maze):  # out of bound check
            if cell.visited:  # not a wall check
                neighbours.append(cell_neighbour)
    return neighbours if neighbours else False


def estimate_cost(goal: Cell, current: Cell) -> int:  # calculate heuristic cost
    return abs(goal.x - current.x) + abs(goal.y - current.x)
