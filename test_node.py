import pytest

from astar import Astar
from maze import Maze
from node import Node, NodeType


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
