from dataclasses import dataclass
from typing import Union, Tuple

import pygame
from pygame import Surface

from cell import Cell, MazeType
from constants import COLS, ROWS, clock


@dataclass
class Maze:
    maze_grid: list[list[Cell]]
    stack: Union[list[Cell], None]
    current_cell: Cell

    @classmethod
    def maze_init(cls) -> 'Maze':
        maze = [[Cell(x=row, y=col) for col in range(COLS)] for row in range(ROWS)]  # maze[x][y] -> Cell(x = x, y = y)
        current_cell = maze[0][0]
        stack = [current_cell]
        current_cell.visited = True
        return cls(maze_grid=maze,
                   stack=stack,
                   current_cell=current_cell)

    def maze_visualise(self, screen: Surface):
        maze = self.maze_grid
        current_cell = self.current_cell
        stack = self.stack
        current_cell.draw(screen=screen)
        while stack:
            directions = current_cell.neighbours_directions(maze=maze)
            next_cells = current_cell.move(directions=directions, maze=maze)
            current_cell.searching = False
            current_cell.draw(screen=screen)
            """
            if there is next cell we put nex cell and path taken in stack, 
            update searching and visited of the next cell and path taken = True then draw cells
            if there is not next cell we roll back the visited cells in stack. and draw cells
            """
            if next_cells:
                for cell in reversed(next_cells):
                    cell.visited = True
                    cell.draw(screen=screen)
                current_cell = next_cells[0]
                current_cell.searching = True
                stack.append(current_cell)
            elif not next_cells:
                current_cell = stack.pop()
                current_cell.searching = True
            current_cell.draw(screen=screen)
            pygame.display.flip()
            clock.tick(20)
        current_cell.searching = False
        [[cell.draw(screen=screen) for cell in maze[i]] for i in range(ROWS)]

    @classmethod
    def maze_generator(cls) -> MazeType:
        """
        same logic as maze_generator, but dose not draw cells
        """
        my_maze = Maze.maze_init()
        maze = my_maze.maze_grid
        current_cell = my_maze.current_cell
        stack = my_maze.stack
        print('non-visualized maze generator')
        while stack:
            directions = current_cell.neighbours_directions(maze=maze)
            next_cells = current_cell.move(directions=directions, maze=maze)
            # next_cell, path = current_cell.walk_to_neighbour(maze=maze)
            if next_cells:
                for cell in reversed(next_cells):
                    cell.visited = True
                current_cell = next_cells[0]
                stack.append(current_cell)
            elif not next_cells and stack:
                current_cell = stack.pop()

        return maze


if __name__ == "__main__":
    tester_maze = Maze.maze_init()
    tester_maze_grid = tester_maze.maze_grid[0]
    print(tester_maze_grid)
