import sys
from dataclasses import dataclass
from typing import Optional

import pygame
from pygame import Surface
from pygame.event import Event

from astar import Astar
from node import Node
from cell import MazeType
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
    node_grid: Optional[Astar] = None

    def events_handler(self, events: list[Event]):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # clear screen
                    self.screen.fill(BLACK)
                    # regenerate maze when press r
                    self.maze_grid[:] = Maze.maze_generator()
                    self.generating = True
                    self.start_point = False
                    self.end_point = False
                if event.key == pygame.K_s:
                    path = self.node_grid.find_path()
                    for point in path[:-1]:
                        point.draw_path(screen=self.screen)
                        pygame.display.flip()
                    # print(f"Path found{path}")

    def visualize_maze(self):
        if self.generating:
            if self.maze_visualization_enable:
                my_maze = Maze.maze_init()
                my_maze.maze_visualise(screen=self.screen)
                self.maze_grid = my_maze.maze_grid
                self.maze_visualization_enable = False
            else:
                [[cells.draw(self.screen) for cells in self.maze_grid[i]] for i in range(ROWS)]
            self.node_grid = Astar.node_init(self.maze_grid)
            print("Maze generated successfully")
            pygame.display.flip()
            self.generating = False

    def place_start_end(self):
        if not self.start_point and not self.end_point:
            begin = self.node_grid.start_node
            end = self.node_grid.goal_node
            begin.is_start = True
            Node.start_node = begin
            end.is_goal = True
            Node.goal_node = end
            self.start_point = True
            self.end_point = True
            begin.draw_start(screen=self.screen)
            end.draw_goal(screen=self.screen)
            pygame.display.flip()
