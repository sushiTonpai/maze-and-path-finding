from typing import Union

import pygame
import sys

from cell import Cell
from constants import WIDTH, HEIGHT, COLS, ROWS, BLACK

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze")
clock = pygame.time.Clock()

# maze = [Cell(row, col) for row in range(ROWS) for col in range(COLS)]
maze: list[list[Cell]] = [[Cell(row, col) for col in range(COLS)] for row in range(ROWS)]
current_cell: Cell = maze[0][0]
stack: Union[list[Cell], None] = [current_cell]
current_cell.in_stack, current_cell.visited = True, True

screen.fill(BLACK)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_cell.draw(screen=screen)
    print(current_cell)

    next_cell, path = current_cell.walk_to_neighbour(maze=maze)

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
    # FPS
    clock.tick(10)
