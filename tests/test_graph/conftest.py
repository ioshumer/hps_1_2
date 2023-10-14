import pytest

from src.graph_10 import SimpleGraph, Vertex


@pytest.fixture(scope="function")
def graph_size():
    return 5


@pytest.fixture(scope='function')
def empty_simple_graph(graph_size) -> SimpleGraph:
    graph = SimpleGraph(graph_size)
    return graph


@pytest.fixture(scope='function')
def full_simple_graph(graph_size) -> SimpleGraph:
    graph = SimpleGraph(graph_size)
    for ctr in range(graph_size):
        graph.AddVertex(ctr)
    return graph


@pytest.fixture(scope='function')
def full_simple_edged_graph(graph_size) -> SimpleGraph:
    graph = SimpleGraph(graph_size)
    for ctr in range(graph_size):
        v = Vertex(ctr)
        v.Value = ctr
        graph.AddVertex(v)
    for x in range(graph_size):
        for y in range(graph_size):
            graph.AddEdge(x, y)
    return graph
