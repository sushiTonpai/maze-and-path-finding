from __future__ import annotations

from dataclasses import dataclass
from typing import Union
from constants import CELL_SIZE, WHITE, YELLOW, GREEN, ROWS, COLS

import random
import pygame


@dataclass
class Cell:
    x: int
    y: int
    visited: bool = False
    in_stack: bool = False

    def draw(self, screen):
        x, y = self.x * CELL_SIZE, self.y * CELL_SIZE
        if self.visited and not self.in_stack:
            pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
        if self.in_stack and self.visited:
            pygame.draw.rect(screen, YELLOW, (x, y, CELL_SIZE, CELL_SIZE))

        # TOP WALL
        pygame.draw.line(screen, GREEN, (x, y), (x + CELL_SIZE, y), 3)
        # BOTTOM WALL
        pygame.draw.line(screen, GREEN, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 3)
        # LEFT WALL
        pygame.draw.line(screen, GREEN, (x, y), (x, y + CELL_SIZE), 3)
        # RIGHT WALL
        pygame.draw.line(screen, GREEN, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 3)

    # find allow neighbour cells
    def walk_to_neighbour(self, maze: Maze) -> Union[tuple[Cell, Cell], tuple[bool,bool]]:
        x, y = self.x, self.y
        # list of walkable cells
        neighbours = {}
        # adjacent cell
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_path = (x + dx, y + dy)
            new_cell = (x + dx * 2, y + dy * 2)
            if 0 <= new_cell[0] < ROWS and 0 <= new_cell[1] < COLS:
                if not maze[new_cell[0]][new_cell[1]].visited:
                    print('visiting = ', new_cell, maze[new_cell[0]][new_cell[1]])
                    neighbours.update({new_cell: new_path})
        if neighbours:
            walk_to_cell, walk_path = random.choice(list(neighbours.items()))
            return maze[walk_to_cell[0]][walk_to_cell[1]], maze[walk_path[0]][walk_path[1]]
        else:
            return False, False


Maze = list[list[Cell]]
