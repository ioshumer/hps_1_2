import pytest

from src.graph_10 import SimpleGraph


def extractor(items):
    return [i.Value for i in items]


def test_remove_edge_0(full_simple_graph):
    result = full_simple_graph.DepthFirstSearch(0, 1)
    assert extractor(result) == []


def test_remove_edge_1(full_simple_graph):
    full_simple_graph.AddEdge(0, 1)
    result = full_simple_graph.DepthFirstSearch(0, 1)
    assert extractor(result) == [0, 1]


def test_remove_edge_2(full_simple_graph):
    full_simple_graph.AddEdge(0, 1)
    full_simple_graph.AddEdge(1, 2)
    result = full_simple_graph.DepthFirstSearch(0, 2)
    assert extractor(result) == [0, 1, 2]


def test_remove_edge_3(full_simple_graph):
    full_simple_graph.AddEdge(0, 1)
    full_simple_graph.AddEdge(1, 2)
    full_simple_graph.AddEdge(0, 3)
    full_simple_graph.AddEdge(3, 4)
    result = full_simple_graph.DepthFirstSearch(0, 4)
    assert extractor(result) == [0, 3, 4]


def test_remove_edge_4(full_simple_graph):
    full_simple_graph.AddEdge(0, 1)
    full_simple_graph.AddEdge(1, 2)
    full_simple_graph.AddEdge(2, 3)
    full_simple_graph.AddEdge(0, 4)
    full_simple_graph.AddEdge(4, 3)
    result = full_simple_graph.DepthFirstSearch(0, 3)
    assert extractor(result) == [0, 1, 2, 3]


def test_remove_edge_5(full_simple_graph):
    full_simple_graph.AddEdge(0, 1)
    full_simple_graph.AddEdge(1, 2)
    result = full_simple_graph.DepthFirstSearch(0, 4)
    assert extractor(result) == []


def test_remove_edge_6(full_simple_graph):
    full_simple_graph.AddEdge(0, 1)
    full_simple_graph.AddEdge(1, 2)
    full_simple_graph.AddEdge(2, 3)
    full_simple_graph.AddEdge(3, 4)
    result = full_simple_graph.DepthFirstSearch(0, 4)
    assert extractor(result) == [0, 1, 2, 3, 4]


def test_remove_edge_7(full_simple_graph):
    full_simple_graph.AddEdge(0, 1)
    full_simple_graph.AddEdge(1, 2)
    full_simple_graph.AddEdge(2, 3)
    full_simple_graph.AddEdge(0, 4)
    full_simple_graph.AddEdge(4, 3)
    result = full_simple_graph.DepthFirstSearch(0, 3)
    assert extractor(result) == [0, 1, 2, 3]


def test_remove_edge_8(full_simple_graph):
    result = full_simple_graph.DepthFirstSearch(0, 4)
    assert extractor(result) == []


def test_remove_edge(full_simple_graph):
    full_simple_graph.AddEdge(0, 0)
    full_simple_graph.AddEdge(0, 1)
    full_simple_graph.AddEdge(2, 2)
    full_simple_graph.AddEdge(4, 0)
    full_simple_graph.AddEdge(4, 1)
    full_simple_graph.AddEdge(4, 2)
    full_simple_graph.AddEdge(4, 3)
    full_simple_graph.AddEdge(4, 4)
    result = full_simple_graph.DepthFirstSearch(0, 2)
    assert extractor(result) == [0, 1, 4, 2]


def test_DFS():
    # Test 1: Basic graph with 2 vertices and 1 edge
    graph = SimpleGraph(2)
    graph.AddVertex(0)
    graph.AddVertex(1)
    graph.AddEdge(0, 1)
    assert extractor(graph.DepthFirstSearch(0, 1)) == [0, 1]

    # Test 2: Graph with 3 vertices and 2 edges forming a path
    graph = SimpleGraph(3)
    graph.AddVertex(0)
    graph.AddVertex(1)
    graph.AddVertex(2)
    graph.AddEdge(0, 1)
    graph.AddEdge(1, 2)
    assert extractor(graph.DepthFirstSearch(0, 2)) == [0, 1, 2]

    # Test 3: Graph with 4 vertices and 3 edges forming a cycle
    graph = SimpleGraph(4)
    graph.AddVertex(0)
    graph.AddVertex(1)
    graph.AddVertex(2)
    graph.AddVertex(3)
    graph.AddEdge(0, 1)
    graph.AddEdge(1, 2)
    graph.AddEdge(2, 0)
    assert extractor(graph.DepthFirstSearch(0, 2)) == [0, 1, 2]

    # Test 4: Graph with disconnected components
    graph = SimpleGraph(5)
    graph.AddVertex(0)
    graph.AddVertex(1)
    graph.AddVertex(2)
    graph.AddVertex(3)
    graph.AddVertex(4)
    graph.AddEdge(0, 1)
    graph.AddEdge(2, 3)
    assert extractor(graph.DepthFirstSearch(0, 3)) == []

    # Test 5: Graph with no edges
    graph = SimpleGraph(2)
    graph.AddVertex(0)
    graph.AddVertex(1)
    assert extractor(graph.DepthFirstSearch(0, 1)) == []
