from dataclasses import dataclass

from node import Node


@dataclass
class Astar:
    node_grid: list[list[Node]]
    start_node: Node
    goal_node: Node
    open_list: list[Node]
    searched_list: list[Node]


    def find_path(self):
        """
        return list of Nodes from start to goal
        """
        pass