import pygame
import sys
import random

# Define constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 40
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Maze generation using Depth-First Search algorithm
def generate_maze():
    maze = [[0] * COLS for _ in range(ROWS)]
    stack = [(0, 0)]

    while stack:
        current_cell = stack[-1]
        maze[current_cell[0]][current_cell[1]] = 1

        neighbors = []
        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_cell = (current_cell[0] + i, current_cell[1] + j)
            if 0 <= new_cell[0] < ROWS and 0 <= new_cell[1] < COLS and maze[new_cell[0]][new_cell[1]] == 0:
                neighbors.append(new_cell)

        if neighbors:
            next_cell = random.choice(neighbors)
            stack.append(next_cell)
        else:
            stack.pop()

    return maze

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Visualization")

# Generate and draw the maze
maze = generate_maze()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    print('blacked')

    for row in range(ROWS):
        for col in range(COLS):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
