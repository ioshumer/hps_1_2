import pytest

from src.graph_8 import SimpleGraph


@pytest.mark.parametrize(
    ('size', 'initial_array', 'required_array'),
    [
        (0, [], []),
        (1, [1], [1]),
        (2, [1, 2], [1, 2]),
        (3, [1, 2, 3], [1, 2, 3]),
        (4, [1, 2, 3, 4], [1, 2, 3, 4]),
        (5, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        (5, [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5]),
    ]
)
def test_graph_creation(size, initial_array, required_array):
    simple_graph = SimpleGraph(size)
    for idx in initial_array:
        simple_graph.AddVertex(idx)
    graph_values = [v.Value for v in simple_graph.vertex]
    assert graph_values == required_array
