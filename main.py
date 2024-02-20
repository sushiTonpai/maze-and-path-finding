import pygame
import sys

from cell import get_start_end
from maze_generator import maze_generator, maze_visualise
from constants import WIDTH, HEIGHT, COLS, ROWS, BLACK, clock

Maze_visualization_enable = False
start_point = False
end_point = False
generating = True


def main():
    # Initialize Pygame
    global Maze_visualization_enable, start_point, end_point, generating
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze")
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
                generating = True
                start_point = False
                end_point = False

        if generating:
            if Maze_visualization_enable:
                maze = maze_visualise(screen)
                Maze_visualization_enable = False
            else:
                [[cells.draw(screen) for cells in maze[i]] for i in range(ROWS)]
                print("Maze visualised successfully")
                pygame.display.flip()
            generating = False

        if not start_point and not end_point:
            start, end = get_start_end(maze)
            start.is_start = True
            end.is_end = True
            start_point, end_point = True, True
            start.draw(screen=screen)
            end.draw(screen=screen)
            pygame.display.flip()
            print(start, end)
        # FPS
        clock.tick(30)


if __name__ == "__main__":
    main()
