import pygame
import sys

from maze_generator import maze_generator, maze_visualise
from constants import WIDTH, HEIGHT, COLS, ROWS, BLACK

Maze_visualization_enable = True


def main():
    # Initialize Pygame
    global Maze_visualization_enable
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze")
    clock = pygame.time.Clock()
    screen.fill(BLACK)

    # generate maze
    maze = maze_generator()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                # clear screen
                screen.fill(BLACK)
                # regenerate maze when press r
                maze = maze_generator()

        # print(current_cell)
        if Maze_visualization_enable:
            maze = maze_visualise(screen)
            Maze_visualization_enable = False
        else:
            [[cells.draw(screen) for cells in maze[i]] for i in range(ROWS)]
            pygame.display.flip()
        # FPS
        clock.tick(30)


if __name__ == "__main__":
    main()
