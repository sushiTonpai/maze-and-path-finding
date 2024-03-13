import pytest
from node import Node


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


def test_calculate_cost(sample_node: Node):
    expected = 7
    got = sample_node.calculate_cost()
    assert expected == got
