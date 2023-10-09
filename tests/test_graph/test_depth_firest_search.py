import pytest


def test_remove_edge_0(full_simple_graph):
    result = full_simple_graph.DepthFirstSearch(0, 1)
    assert result == []


def test_remove_edge_1(full_simple_graph):
    full_simple_graph.AddEdge(0, 1)
    result = full_simple_graph.DepthFirstSearch(0, 1)
    assert result == [0, 1]


def test_remove_edge_2(full_simple_graph):
    full_simple_graph.AddEdge(0, 1)
    full_simple_graph.AddEdge(1, 2)
    result = full_simple_graph.DepthFirstSearch(0, 2)
    assert result == [0, 1, 2]


def test_remove_edge_3(full_simple_graph):
    full_simple_graph.AddEdge(0, 1)
    full_simple_graph.AddEdge(1, 2)
    full_simple_graph.AddEdge(0, 3)
    full_simple_graph.AddEdge(3, 4)
    result = full_simple_graph.DepthFirstSearch(0, 4)
    assert result == [0, 3, 4]


def test_remove_edge_4(full_simple_graph):
    full_simple_graph.AddEdge(0, 1)
    full_simple_graph.AddEdge(1, 2)
    full_simple_graph.AddEdge(2, 3)
    full_simple_graph.AddEdge(0, 4)
    full_simple_graph.AddEdge(4, 3)
    result = full_simple_graph.DepthFirstSearch(0, 3)
    assert result == [0, 1, 2, 3]


def test_remove_edge_5(full_simple_graph):
    full_simple_graph.AddEdge(0, 1)
    full_simple_graph.AddEdge(1, 2)
    result = full_simple_graph.DepthFirstSearch(0, 4)
    assert result == []


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
    assert result == [0, 1, 4, 2]
