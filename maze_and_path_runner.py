import sys
from dataclasses import dataclass

import pygame
from pygame import Surface
from pygame.event import Event

from cell import Cell, get_start_end
from constants import BLACK, ROWS
from maze import maze_generator, maze_visualise


@dataclass
class MazeAndPathRunner:
    screen: Surface
    maze: list[list[Cell]]
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
                self.maze[:] = maze_generator()
                self.generating = True
                self.start_point = False
                self.end_point = False

    def visualize_maze(self):
        if self.generating:
            if self.maze_visualization_enable:
                self.maze = maze_visualise(self.screen)
                self.maze_visualization_enable = False
            else:
                [[cells.draw(self.screen) for cells in self.maze[i]] for i in range(ROWS)]
                print("Maze visualised successfully")
            pygame.display.flip()
            self.generating = False

    def place_start_end(self):
        if not self.start_point and not self.end_point:
            start, end = get_start_end(self.maze)
            start.is_start = True
            end.is_end = True
            self.start_point = True
            self.end_point = True
            start.draw(screen=self.screen)
            end.draw(screen=self.screen)
            pygame.display.flip()
            print(start, end)
