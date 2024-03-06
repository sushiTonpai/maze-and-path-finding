from __future__ import annotations

from dataclasses import dataclass
from typing import Union
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
    x: int
    y: int
    visited: bool = False
    searching: bool = False
    is_start: bool = False
    is_goal: bool = False

    def draw(self, screen):
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
        if self.visited and self.is_start:
            """
            draw blue circle at starting point
            """
            pygame.draw.circle(screen, BLUE, (x + (0.5 * CELL_SIZE), y + (0.5 * CELL_SIZE)), 1 / 4 * CELL_SIZE)

        if self.visited and self.is_goal:
            """
            draw red circle at starting point
            """
            pygame.draw.circle(screen, RED, (x + (0.5 * CELL_SIZE), y + (0.5 * CELL_SIZE)), 1 / 4 * CELL_SIZE)

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

        if move_direction == 'north':
            return move_helper(0, -2)
        if move_direction == 'south':
            return move_helper(0, 2)
        if move_direction == 'east':
            return move_helper(2, 0)
        if move_direction == 'west':
            return move_helper(-2, 0)

    def walk_to_neighbour(self, maze: MazeType) -> Union[tuple[Cell, Cell], tuple[bool, bool]]:

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
            if 0 <= new_cell[0] < COLS and 0 <= new_cell[1] < ROWS:
                if not maze[new_cell[0]][new_cell[1]].visited:
                    # print('visiting = ', new_cell, maze[new_cell[0]][new_cell[1]])
                    neighbours.update({new_cell: new_path})
        # check item in neighbours if not return False
        if neighbours:
            print(neighbours)
            walk_to_cell, walk_path = random.choice(list(neighbours.items()))
            return maze[walk_to_cell[0]][walk_to_cell[1]], maze[walk_path[0]][walk_path[1]]
        else:
            return False, False


def get_start_end(maze: MazeType):
    lst_of_visited = []
    for row in range(ROWS):
        for col in range(COLS):
            if maze[row][col].visited:
                lst_of_visited.append(maze[row][col])
    start = random.choice(lst_of_visited)
    lst_of_visited.remove(start)
    end = random.choice(lst_of_visited)
    return start, end


# Type annotation
MazeType = list[list[Cell]]
