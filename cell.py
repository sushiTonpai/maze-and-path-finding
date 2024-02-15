from __future__ import annotations

from dataclasses import dataclass
from typing import Union
from constants import CELL_SIZE, WHITE, YELLOW, GREEN, ROWS, COLS

import random
import pygame

'''
the Cell class have draw and walk_to_neighbor functions:
draw is to draw block with green walls
    cell block background yellow = searching path(in stack)
    cell block background white = done searching path(not in stack)
    
walk_to_neighbor is function that return walkable cell with path taken
    eg. walk south from Cell(0, 0) ->
            walk_to_cell = (0,2), walk_path = (0,1)
        walk west from Cell (4,5) ->
            walk_to_cell = (2,5), walk_path = (3,5)
'''


@dataclass
class Cell:
    x: int
    y: int
    visited: bool = False
    in_stack: bool = False

    def draw(self, screen):
        # pixel position of cell = x,y
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
    def walk_to_neighbour(self, maze: Maze) -> Union[tuple[Cell, Cell], tuple[bool, bool]]:
        """
        neighbour is dict contain key of walkable call with value of path taken then choose randomly in neighbour
        dict
        return walk_to_cell = Cell or False if nothing in neighbour dict , walk_path = Cell or False if nothing
        in neighbour dict
        :param maze:
        """
        x, y = self.x, self.y
        # dict of walkable cells
        neighbours = {}
        # adjacent cell
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            # new path and cell in direction of dx and dy
            new_path = (x + dx, y + dy)
            new_cell = (x + dx * 2, y + dy * 2)
            # out of bound check and Cell is visited
            if 0 <= new_cell[0] < ROWS and 0 <= new_cell[1] < COLS:
                if not maze[new_cell[0]][new_cell[1]].visited:
                    # print('visiting = ', new_cell, maze[new_cell[0]][new_cell[1]])
                    neighbours.update({new_cell: new_path})
        # check item in neighbours if not return False
        if neighbours:
            walk_to_cell, walk_path = random.choice(list(neighbours.items()))
            return maze[walk_to_cell[0]][walk_to_cell[1]], maze[walk_path[0]][walk_path[1]]
        else:
            return False, False


# Type annotation
Maze = list[list[Cell]]
