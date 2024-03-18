from __future__ import annotations
from dataclasses import dataclass
import random
from typing import Optional

import pygame
from pygame import Surface

from cell import Cell
from constants import COLS, ROWS, BLUE, CELL_SIZE, RED, YELLOW


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
    parents: Optional[Node] = None
    is_wall: bool = False
    g_cost: float = float('inf')
    h_cost: int = 0
    f_cost: float = float('inf')

    @classmethod
    def cell_to_node(cls, cell: Cell) -> Node:
        """
        initialise node from Cell
        """
        return cls(node_x=cell.x, node_y=cell.y, is_wall=not cell.visited)

    def calculate_cost(self):
        return self.h_cost + self.g_cost

    def estimate_cost(self, target: Node) -> int:  # calculate heuristic cost
        return abs(target.node_x - self.node_x) + abs(target.node_y - self.node_y)

    def draw_start(self, screen: Surface):
        x = self.node_x * CELL_SIZE
        y = self.node_y * CELL_SIZE

        pygame.draw.circle(screen, BLUE, (x + (0.5 * CELL_SIZE), y + (0.5 * CELL_SIZE)), 1 / 4 * CELL_SIZE)

    def draw_goal(self, screen: Surface):
        x = self.node_x * CELL_SIZE
        y = self.node_y * CELL_SIZE

        pygame.draw.circle(screen, RED, (x + (0.5 * CELL_SIZE), y + (0.5 * CELL_SIZE)), 1 / 4 * CELL_SIZE)

    def draw_path(self, screen: Surface):
        """
        Draw path on maze
        """
        x = self.node_x * CELL_SIZE
        y = self.node_y * CELL_SIZE
        pygame.draw.rect(screen, YELLOW, (x, y, CELL_SIZE, CELL_SIZE))

    def __lt__(self, other):
        return self.g_cost < other.g_cost


def get_start_end(nodes: list[list[Node]]) -> tuple[Node, Node]:
    not_walls: list[Node] = []
    for row in range(len(nodes)):
        for col in range(len(nodes[0])):
            if not nodes[row][col].is_wall:
                not_walls.append(nodes[row][col])
    if not_walls:
        start = random.choice(not_walls)
        not_walls.remove(start)
        end = random.choice(not_walls)
        return start, end
    return nodes[0][0], nodes[-1][-1]


NodeType = list[list[Node]]
