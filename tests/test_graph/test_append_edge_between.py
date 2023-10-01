import pytest


@pytest.mark.parametrize(
    ('v1', 'v2'),
    [
        (0, 0),
        (1, 1),
        (1, 2),
        (2, 2),
        (4, 0),
        (4, 1),
        (4, 2),
        (4, 3),
        (4, 4),
    ]
)
def test_append_edge(v1, v2, full_simple_graph):
    full_simple_graph.AddEdge(v1, v2)
    assert full_simple_graph.m_adjacency[v1][v2] == 1
    assert full_simple_graph.m_adjacency[v2][v1] == 1
    assert full_simple_graph.IsEdge(v1, v2)
