from typing import Union

import pygame
import sys

from maze_generator import maze_generator
from cell import Cell
from constants import WIDTH, HEIGHT, COLS, ROWS, BLACK

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze")
clock = pygame.time.Clock()
screen.fill(BLACK)


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # print(current_cell)
    maze_generator()
    pygame.display.flip()
    # FPS
    clock.tick(30)
