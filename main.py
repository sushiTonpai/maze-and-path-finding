import pygame
from maze_and_path_runner import MazeAndPathRunner
from maze import maze_generator
from constants import WIDTH, HEIGHT, COLS, ROWS, BLACK, clock


def main(
        maze_visualization_enable=False,
        start_point=False,
        end_point=False,
        generating=True,
):
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze")
    screen.fill(BLACK)

    maze_and_path = MazeAndPathRunner(
        screen=screen,
        maze=maze_generator(),  # generate maze
        generating=generating,
        start_point=start_point,
        end_point=end_point,
        maze_visualization_enable=maze_visualization_enable,
    )

    # Main game loop
    while True:
        events = pygame.event.get()
        maze_and_path.events_handler(events=events)
        maze_and_path.visualize_maze()
        maze_and_path.place_start_end()
        # FPS
        clock.tick(30)


if __name__ == "__main__":
    main(maze_visualization_enable=True)
