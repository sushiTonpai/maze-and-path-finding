from dataclasses import dataclass

from cell import Cell, MazeType


@dataclass
class Astar:
    """
    A* algorithm F(n) = G(n) + H(n) where n is Cell
    F(n) represents the total cost of that node
    G(n) represents the distance to that node from the starting node
    H(n) represents the estimate distance to goal
    H(n) distance calculate by manhattan distance -> abs(current.x - goal.x) + abs(current.y - goal.y)

    """
    distance_cost: int
    h_cost: int
    total_cost: int


def walkable_path(cell, maze) -> list[Cell] or bool:
    neighbours = []
    # 4 direction [(west)(east)(north)(south)]
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        cell_neighbour = cell.x + dx, cell.y + dy
        if 0 <= cell_neighbour[0] < len(maze[0]) and 0 <= cell_neighbour[1] < len(maze):  # out of bound check
            if cell.visited:  # not a wall check
                neighbours.append(cell_neighbour)
    return neighbours if neighbours else False


def distance_to_node(start: Cell, current: Cell, maze: MazeType) -> int:  # calculate G(n) cost
    return 1


def estimate_cost(goal: Cell, current: Cell, maze: MazeType) -> int:    # calculate heuristic cost
    return abs(goal.x - current.x) + abs(goal.y - current.x)
