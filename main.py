from typing import Union

import pygame
import sys

from maze_generator import maze_generator
from cell import Cell
from constants import WIDTH, HEIGHT, COLS, ROWS, BLACK


def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze")
    clock = pygame.time.Clock()
    screen.fill(BLACK)

    maze = maze_generator()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # print(current_cell)

        [[cells.draw(screen) for cells in maze[i]] for i in range(ROWS)]
        # pygame.display.flip()
        # FPS
        clock.tick(30)


if __name__ == "__main__":
    main()
