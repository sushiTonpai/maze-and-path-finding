from typing import Union, Tuple

import pygame
from pygame import Surface

from cell import Cell, MazeType
from constants import COLS, ROWS, clock


class Maze:
    """
    Maze class with class methods
    """


def maze_init() -> Tuple[MazeType, list[Cell], Cell]:
    """
    Initializes the Maze with starting current cell at maze[0][0] and empty stack
    :return: maze: Maze, stack: List, current cell: Cell
    """
    maze: list[list[Cell]] = [[Cell(row, col) for col in range(COLS)] for row in range(ROWS)]
    stack: Union[list[Cell], None] = [maze[0][0]]
    current_cell: Cell = maze[0][0]
    current_cell.visited, current_cell.in_stack = True, True
    return maze, stack, current_cell


def maze_visualise(screen: Surface):
    maze, stack, current_cell = maze_init()
    current_cell.draw(screen=screen)
    while stack:
        next_cell, path = current_cell.walk_to_neighbour(maze=maze)
        """
        if there is next cell we put nex cell and path taken in stack, 
        update in_stack and visited of the next cell and path taken = True then draw cells
        if there is not next cell we roll back the visited cells in stack. and draw cells
        """
        if next_cell:
            current_cell = next_cell
            path.in_stack, path.visited = True, True
            current_cell.in_stack, current_cell.visited = True, True
            stack.append(path)
            stack.append(current_cell)
            path.draw(screen=screen)
            current_cell.draw(screen=screen)
        elif not next_cell and stack:
            current_cell = stack.pop()
            current_cell.in_stack = False
            current_cell.draw(screen=screen)
            if len(stack) > 1:
                path = stack.pop()
                path.in_stack = False
                path.draw(screen=screen)
        pygame.display.flip()
        clock.tick(10)
    [[cell.draw(screen=screen) for cell in maze[i]] for i in range(ROWS)]
    return maze


def maze_generator() -> MazeType:
    """
    same logic as maze_generator, but dose not draw cells
    """
    maze, stack, current_cell = maze_init()
    while stack:
        next_cell, path = current_cell.walk_to_neighbour(maze=maze)
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
