import pytest


@pytest.mark.parametrize(
    'value',
    [
        0, 1, 2, 3, 4
    ]
)
def test_remove_vertex(value, full_simple_edged_graph):
    full_simple_edged_graph.RemoveVertex(value)
    for idx in range(full_simple_edged_graph.max_vertex):
        assert full_simple_edged_graph.m_adjacency[value][idx] is None
        assert full_simple_edged_graph.m_adjacency[idx][value] is None
        assert not full_simple_edged_graph.IsEdge(value, idx)
        assert not full_simple_edged_graph.IsEdge(idx, value)
