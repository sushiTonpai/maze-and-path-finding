import pygame
import sys

from cell import Cell
from constants import WIDTH, HEIGHT, COLS, ROWS, BLACK

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze")
clock = pygame.time.Clock()

# initial pygame setup
maze: list[list[Cell]] = [[Cell(row, col) for col in range(COLS)] for row in range(ROWS)]
current_cell = maze[0][0]
stack = [current_cell]
current_cell.visited = True
current_cell.in_stack = True

screen.fill(BLACK)

# Main game loop
while True:
    # exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_cell.draw(screen=screen)
    # print(current_cell)

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
        # stack.append(path)
        stack.append(current_cell)
        path.draw(screen=screen)
        current_cell.draw(screen=screen)
    elif not next_cell and stack:
        current_cell = stack.pop()
        # path = stack.pop()
        current_cell.in_stack = False
        current_cell.draw(screen=screen)

    pygame.display.flip()
    clock.tick(10)
