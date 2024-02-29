import sys
from dataclasses import dataclass

import pygame
from pygame import Surface
from pygame.event import Event

from cell import Cell, get_start_end, MazeType
from constants import BLACK, ROWS
from maze import Maze


@dataclass
class MazeAndPathRunner:
    screen: Surface
    maze_grid: MazeType
    generating: bool
    start_point: bool
    end_point: bool
    maze_visualization_enable: bool

    def events_handler(self, events: list[Event]):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                # clear screen
                self.screen.fill(BLACK)
                # regenerate maze when press r
                self.maze_grid[:] = Maze.maze_generator()
                self.generating = True
                self.start_point = False
                self.end_point = False

    def visualize_maze(self):
        if self.generating:
            if self.maze_visualization_enable:
                my_maze = Maze.maze_init()
                my_maze.maze_visualise(screen=self.screen)
                self.maze_grid = my_maze.maze_grid
                self.maze_visualization_enable = False
            else:
                [[cells.draw(self.screen) for cells in self.maze_grid[i]] for i in range(ROWS)]
            print("Maze generated successfully")
            pygame.display.flip()
            self.generating = False

    def place_start_end(self):
        if not self.start_point and not self.end_point:
            start, end = get_start_end(self.maze_grid)
            start.is_start = True
            end.is_goal = True
            self.start_point = True
            self.end_point = True
            start.draw(screen=self.screen)
            end.draw(screen=self.screen)
            pygame.display.flip()
