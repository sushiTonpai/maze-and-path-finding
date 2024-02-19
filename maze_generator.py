from typing import Union

import pygame

from cell import Cell
from constants import COLS, ROWS


def maze_generator():
    maze: list[list[Cell]] = [[Cell(row, col) for col in range(COLS)] for row in range(ROWS)]
    stack: Union[list[Cell], None] = [maze[0][0]]
    current_cell: Cell = maze[0][0]
    current_cell.visited, current_cell.in_stack = True, True

    next_cell, path = current_cell.walk_to_neighbour(maze=maze)
    """
    if there is next cell we put nex cell and path taken in stack, 
    update in_stack and visited of the next cell and path taken = True then draw cells
    if there is not next cell we roll back the visited cells in stack. and draw cells
    """
    while stack:
        if next_cell:
            current_cell = next_cell
            path.in_stack, path.visited = True, True
            current_cell.in_stack, current_cell.visited = True, True
            stack.append(path)
            stack.append(current_cell)
        elif not next_cell and stack:
            current_cell = stack.pop()
            current_cell.in_stack = False
            if len(stack) > 1:
                path = stack.pop()
                path.in_stack = False
    return maze
