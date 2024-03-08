from __future__ import annotations
from dataclasses import dataclass, asdict

from cell import Cell, MazeType
from constants import COLS, ROWS


@dataclass
class Node:
    """
    A* algorithm F(n) = G(n) + H(n) where n is Cell
    F(n) represents the total cost of that node
    G(n) represents the distance to that node from the starting node
    H(n) represents the estimate distance to goal
    H(n) distance calculate by manhattan distance -> abs(current.x - goal.x) + abs(current.y - goal.y)

    """

    node_x: int
    node_y: int
    parents: Node = None
    is_wall: bool = False
    g_cost: int = 99999
    h_cost: int = 99999
    f_cost: int = 99999

    @classmethod
    def cell_to_node(cls, cell: Cell) -> Node:
        """
        initialise node from Cell
        """
        return cls(node_x=cell.x, node_y=cell.y, is_wall=not cell.visited)

    def calculate_cost(self):
        return self.h_cost + self.g_cost

    def estimate_cost(self, target: Node):  # calculate heuristic cost
        self.h_cost = abs(target.node_x - self.node_x) + abs(target.node_y - self.node_y)

