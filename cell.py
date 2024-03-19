from __future__ import annotations

from dataclasses import dataclass

from pygame import Surface

from constants import CELL_SIZE, WHITE, YELLOW, GREEN, ROWS, COLS, BLUE, RED

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
    """
    Cell class represents cell in maze

    Attributes:
        x (int): x coordinate of the cell
        y (int): y coordinate of the cell
        visited (bool): whether cell is visited or not
        searching (bool): whether cell is searching/ most front cell
        is_start (bool): whether cell is starting cell
        is_goal (bool): whether cell is end goal cell
    """
    x: int
    y: int
    visited: bool = False
    searching: bool = False
    is_start: bool = False
    is_goal: bool = False

    def draw(self, screen: Surface):
        # pixel position of cell = x,y
        x, y = self.x * CELL_SIZE, self.y * CELL_SIZE

        if self.visited:
            pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
        if self.searching and self.visited:
            pygame.draw.rect(screen, YELLOW, (x, y, CELL_SIZE, CELL_SIZE))
        if not self.visited:
            """
            draw walls with thickness of 10% of cell size
            """
            # TOP WALL
            pygame.draw.line(screen, GREEN, (x, y), (x + CELL_SIZE, y), int(1 / 10 * CELL_SIZE))
            # BOTTOM WALL
            pygame.draw.line(screen, GREEN, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), int(1 / 10 * CELL_SIZE))
            # LEFT WALL
            pygame.draw.line(screen, GREEN, (x, y), (x, y + CELL_SIZE), int(1 / 10 * CELL_SIZE))
            # RIGHT WALL
            pygame.draw.line(screen, GREEN, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), int(1 / 10 * CELL_SIZE))

    # find allow neighbour cells
    def neighbours_directions(self, maze: MazeType) -> list[str]:
        """
        return a list of all visitable neighbors in four directions north, south, east, west
        """
        x, y = self.x, self.y
        neighbors = []

        def add_neighbour(dx, dy, direction):
            nx, ny = x + dx, y + dy
            if 0 <= nx < COLS and 0 <= ny < ROWS and not maze[nx][ny].visited:
                neighbors.append(direction)

        # north check
        add_neighbour(0, -2, 'north')
        # south check
        add_neighbour(0, 2, 'south')
        # east check
        add_neighbour(2, 0, 'east')
        # west check
        add_neighbour(-2, 0, 'west')

        return neighbors

    def move(self, directions: list[str], maze: MazeType) -> list[Cell] or bool:
        """
        return a list of cell representing new cell and path taken
        where return list[0] = new cell and list[1] = new path
        function return False if directions is empty
        """
        if len(directions) > 0:
            move_direction = random.choice(directions)
        else:
            return False

        def move_helper(dx, dy):
            return [maze[self.x + dx][self.y + dy], maze[self.x + dx // 2][self.y + dy // 2]]

        match move_direction:
            case 'north':
                return move_helper(0, -2)
            case 'south':
                return move_helper(0, 2)
            case 'east':
                return move_helper(2, 0)
            case 'west':
                return move_helper(-2, 0)


# Type annotation
MazeType = list[list[Cell]]
