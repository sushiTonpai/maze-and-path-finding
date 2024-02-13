import pygame
import sys
import random
from dataclasses import dataclass

# Define constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 40
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (129, 0, 0)


@dataclass
class Cell:
    x: int
    y: int
    visited: bool = False
    in_stack: bool = False

    def draw(self):
        x, y = self.x * CELL_SIZE, self.y * CELL_SIZE
        if self.visited and not self.in_stack:
            pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
        if self.in_stack and self.visited:
            pygame.draw.rect(screen, YELLOW, (x, y, CELL_SIZE, CELL_SIZE))

        # TOP WALL
        pygame.draw.line(screen, GREEN, (x, y), (x + CELL_SIZE, y), 3)
        # BOTTOM WALL
        pygame.draw.line(screen, GREEN, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 3)
        # LEFT WALL 
        pygame.draw.line(screen, GREEN, (x, y), (x, y + CELL_SIZE), 3)
        # RIGHT WALL
        pygame.draw.line(screen, GREEN, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 3)

    # find allow neighbour cells
    def walk_to_neighbour(self, maze):
        x, y = self.x, self.y
        neighbours = []
        # adjacent cell
        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_cell = (x + i, y + j)
            if 0 <= new_cell[0] < ROWS and 0 <= new_cell[1] < COLS:
                if not maze[new_cell[0]][new_cell[1]].visited:
                    print('visiting = ', new_cell, maze[new_cell[0]][new_cell[1]])
                    neighbours.append(new_cell)
        if neighbours:
            walk_to_cell = random.choice(neighbours)
            return maze[walk_to_cell[0]][walk_to_cell[1]]
        else:
            return False


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze")
clock = pygame.time.Clock()

# maze = [Cell(row, col) for row in range(ROWS) for col in range(COLS)]
maze = [[Cell(row, col) for col in range(COLS)] for row in range(ROWS)]
current_cell = maze[0][0]
stack = [current_cell]
current_cell.visited = True
current_cell.in_stack = True

screen.fill(BLACK)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # [Cell(row, col).draw() for row in range(ROWS) for col in range(COLS)]
    current_cell.draw()
    print(current_cell)

    next_cell = current_cell.walk_to_neighbour(maze=maze)

    if next_cell:
        current_cell = next_cell
        current_cell.visited = True
        current_cell.in_stack = True
        stack.append(current_cell)
        current_cell.draw()
    elif not next_cell and stack:
        current_cell = stack.pop()
        current_cell.in_stack = False
        current_cell.draw()

    pygame.display.flip()
    clock.tick(15)
