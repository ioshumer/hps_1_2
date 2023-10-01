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
def test_remove_edge(v1, v2, full_simple_edged_graph):
    full_simple_edged_graph.RemoveEdge(v1, v2)
    assert full_simple_edged_graph.m_adjacency[v1][v2] is None
    assert full_simple_edged_graph.m_adjacency[v2][v1] is None
    assert not full_simple_edged_graph.IsEdge(v1, v2)
