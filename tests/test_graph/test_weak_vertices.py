from src.graph_12 import SimpleGraph


def extractor(items):
    return [i.Value for i in items]


def test_1(full_simple_graph):
    full_simple_graph.AddEdge(0, 1)
    full_simple_graph.AddEdge(1, 2)
    full_simple_graph.AddEdge(1, 2)
    full_simple_graph.AddEdge(2, 3)
    full_simple_graph.AddEdge(2, 4)
    full_simple_graph.AddEdge(3, 4)
    WeakVertices = full_simple_graph.WeakVertices()
    assert extractor(WeakVertices) == [0, 1]


