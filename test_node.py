import random
from typing import List

import pytest

from astar import Astar
from maze import Maze
from node import Node, NodeType
from cell import Cell, MazeType


@pytest.fixture()
def sample_node() -> Node:
    return Node(
        node_x=1,
        node_y=2,
        parents=None,
        is_wall=False,
        g_cost=3,
        h_cost=4,
        f_cost=5,
    )


@pytest.fixture()
def sample_astar_node_grid() -> Astar:
    test_maze = Maze.maze_generator()
    nodes = Astar.node_init(test_maze)
    return nodes


@pytest.fixture()
def simple_maze() -> MazeType:
    simple_maze = [[Cell(x=row, y=col) for col in range(3)] for row in range(3)]
    return simple_maze


@pytest.fixture()
def sample_maze() -> MazeType:
    return [
        [Cell(x=0, y=0, visited=True, searching=False, is_start=False, is_goal=False),
  Cell(x=0, y=1, visited=True, searching=False, is_start=False, is_goal=False),
  Cell(x=0, y=2, visited=True, searching=False, is_start=False, is_goal=False),
  Cell(x=0, y=3, visited=True, searching=False, is_start=False, is_goal=False),
  Cell(x=0, y=4, visited=True, searching=False, is_start=False, is_goal=False)],
        [Cell(x=1, y=0, visited=False, searching=False, is_start=False, is_goal=False),
  Cell(x=1, y=1, visited=False, searching=False, is_start=False, is_goal=False),
  Cell(x=1, y=2, visited=False, searching=False, is_start=False, is_goal=False),
  Cell(x=1, y=3, visited=False, searching=False, is_start=False, is_goal=False),
  Cell(x=1, y=4, visited=True, searching=False, is_start=False, is_goal=False)],
        [Cell(x=2, y=0, visited=True, searching=False, is_start=False, is_goal=False),
  Cell(x=2, y=1, visited=True, searching=False, is_start=False, is_goal=False),
  Cell(x=2, y=2, visited=True, searching=False, is_start=False, is_goal=False),
  Cell(x=2, y=3, visited=False, searching=False, is_start=False, is_goal=False),
  Cell(x=2, y=4, visited=True, searching=False, is_start=False, is_goal=False)],
        [Cell(x=3, y=0, visited=True, searching=False, is_start=False, is_goal=False),
  Cell(x=3, y=1, visited=False, searching=False, is_start=False, is_goal=False),
  Cell(x=3, y=2, visited=True, searching=False, is_start=False, is_goal=False),
  Cell(x=3, y=3, visited=False, searching=False, is_start=False, is_goal=False),
  Cell(x=3, y=4, visited=False, searching=False, is_start=False, is_goal=False)],
        [Cell(x=4, y=0, visited=True, searching=False, is_start=False, is_goal=False),
  Cell(x=4, y=1, visited=False, searching=False, is_start=False, is_goal=False),
  Cell(x=4, y=2, visited=True, searching=False, is_start=False, is_goal=False),
  Cell(x=4, y=3, visited=True, searching=False, is_start=False, is_goal=False),
  Cell(x=4, y=4, visited=True, searching=False, is_start=False, is_goal=False)]
            ]


def test_simple_maze(simple_maze: MazeType):
    assert len(simple_maze) == 3 and len(simple_maze[0]) == 3


def test_simple_astar_node_grid(simple_maze: MazeType):
    simple_nodes = Astar.node_init(simple_maze)
    assert len(simple_nodes.node_grid) == len(simple_maze)


def test_walkable_neighbors_empty(simple_maze: MazeType):
    simple_nodes = Astar.node_init(simple_maze)
    neighbors = Astar.walkable_neighbours(simple_nodes, simple_nodes.node_grid[0][0])
    assert neighbors == []


def test_walkable_neighbors(sample_maze: MazeType):
    sample_nodes = Astar.node_init(sample_maze)
    neighbors = Astar.walkable_neighbours(sample_nodes, sample_nodes.node_grid[0][0])
    assert neighbors == [sample_nodes.node_grid[0][1]]

def test_node_init_len():
    test_maze = Maze.maze_generator()
    nodes = Astar.node_init(test_maze)
    assert len(nodes.node_grid) == len(test_maze)


def test_node_init_first_row_xy():
    test_maze = Maze.maze_generator()
    nodes = Astar.node_init(test_maze).node_grid
    for cell, node in zip(test_maze[0], nodes[0]):
        assert cell.x == node.node_x and cell.y == node.node_y


def test_start_end_placement_not_blocked(sample_astar_node_grid: Astar):
    start = sample_astar_node_grid.start_node
    goal = sample_astar_node_grid.goal_node
    assert not start.is_wall and not goal.is_wall


def test_calculate_cost(sample_node: Node):
    expected = 7
    got = sample_node.calculate_cost()
    assert expected == got
