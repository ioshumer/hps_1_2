import pytest

from src.trees_1 import SimpleTreeNode, SimpleTree


def test_appending_node():
    RootNode = SimpleTreeNode(15, None)
    Tree = SimpleTree(RootNode)

    NewNode = SimpleTreeNode(27, None)
    Tree.AddChild(RootNode, NewNode)

    assert Tree.Root == RootNode
    assert Tree.Root.Children == [NewNode]


def test_remove_nonroot():
    RootNode = SimpleTreeNode(15, None)
    Tree = SimpleTree(RootNode)

    NewNode = SimpleTreeNode(27, None)
    Tree.AddChild(RootNode, NewNode)

    Tree.DeleteNode(NewNode)

    assert Tree.Root.Children == []


def test_traverse_tree():
    RootNode = SimpleTreeNode(15, None)

    Tree = SimpleTree(RootNode)

    LeftNode = SimpleTreeNode(7, None)
    RightNode = SimpleTreeNode(21, None)

    Tree.AddChild(RootNode, LeftNode)
    Tree.AddChild(RootNode, RightNode)

    RightNodeA = SimpleTreeNode(19, None)
    RightNodeB = SimpleTreeNode(23, None)

    RightNodeB_1 = SimpleTreeNode(15, None)

    Tree.AddChild(RightNode, RightNodeA)
    Tree.AddChild(RightNode, RightNodeB)

    Tree.AddChild(RightNodeB, RightNodeB_1)

    ethalon = [
        {RootNode: [
            {LeftNode: []},
            {RightNode: [
                {RightNodeA: []},
                {RightNodeB: [
                    {RightNodeB_1: []}
                ]}
            ]}
        ]}
    ]
    AllNodes = Tree.GetAllNodes()
    assert AllNodes == ethalon


def test_move_node():
    RootNode = SimpleTreeNode(15, None)

    LeftNode = SimpleTreeNode(7, None)
    RightNode = SimpleTreeNode(21, None)

    Tree = SimpleTree(RootNode)
    Tree.AddChild(RootNode, LeftNode)
    Tree.AddChild(RootNode, RightNode)

    RightNodeA = SimpleTreeNode(19, None)
    RightNodeB = SimpleTreeNode(23, None)

    RightNodeB_1 = SimpleTreeNode(15, None)

    Tree.AddChild(RightNode, RightNodeA)
    Tree.AddChild(RightNode, RightNodeB)

    Tree.AddChild(RightNodeB, RightNodeB_1)

    Ethalon = [
        {RootNode: [
            {LeftNode: []},
            {RightNode: [
                {RightNodeA: []},
                {RightNodeB: [
                    {RightNodeB_1: []}
                ]}
            ]}
        ]}
    ]
    assert Tree.GetAllNodes() == Ethalon

    Tree.MoveNode(RightNodeB, LeftNode)
    MovedEthalon = [
        {RootNode: [
            {LeftNode: [
                {RightNodeB: [
                    {RightNodeB_1: []}
                ]}
            ]},
            {RightNode: [
                {RightNodeA: []}
            ]}
        ]}
    ]
    assert Tree.GetAllNodes() == MovedEthalon


def test_find_node():
    RootNode = SimpleTreeNode(15, None)

    LeftNode = SimpleTreeNode(7, None)
    RightNode = SimpleTreeNode(21, None)

    Tree = SimpleTree(RootNode)
    Tree.AddChild(RootNode, LeftNode)
    Tree.AddChild(RootNode, RightNode)

    RightNodeA = SimpleTreeNode(19, None)
    RightNodeB = SimpleTreeNode(23, None)

    RightNodeB_1 = SimpleTreeNode(15, None)

    Tree.AddChild(RightNode, RightNodeA)
    Tree.AddChild(RightNode, RightNodeB)

    Tree.AddChild(RightNodeB, RightNodeB_1)

    FindedNodes15 = Tree.FindNodesByValue(15)

    assert len(FindedNodes15) == 2
    assert FindedNodes15 == [RootNode, RightNodeB_1]

    FindedNodes333 = Tree.FindNodesByValue(333)
    assert len(FindedNodes333) == 0
    assert FindedNodes333 == []


def test_count_node_and_leafs():
    RootNode = SimpleTreeNode(15, None)
    Tree = SimpleTree(RootNode)
    assert Tree.Count() == 0
    assert Tree.LeafCount() == 1

    LeftNode = SimpleTreeNode(7, None)
    Tree.AddChild(RootNode, LeftNode)
    assert Tree.Count() == 1
    assert Tree.LeafCount() == 1

    RightNode = SimpleTreeNode(21, None)
    Tree.AddChild(RootNode, RightNode)
    assert Tree.Count() == 1
    assert Tree.LeafCount() == 2

    RightNodeA = SimpleTreeNode(19, None)
    Tree.AddChild(RightNode, RightNodeA)
    assert Tree.Count() == 2
    assert Tree.LeafCount() == 2

    RightNodeB = SimpleTreeNode(23, None)
    Tree.AddChild(RightNode, RightNodeB)
    assert Tree.Count() == 2
    assert Tree.LeafCount() == 3

    RightNodeB_1 = SimpleTreeNode(15, None)
    Tree.AddChild(RightNodeB, RightNodeB_1)
    assert Tree.Count() == 3
    assert Tree.LeafCount() == 3


