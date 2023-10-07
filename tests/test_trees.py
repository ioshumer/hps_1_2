from src.trees_9 import SimpleTreeNode, SimpleTree


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
        RootNode, LeftNode, RightNode,
        RightNodeA, RightNodeB, RightNodeB_1
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
        RootNode, LeftNode, RightNode, RightNodeA, RightNodeB, RightNodeB_1
    ]
    assert Tree.GetAllNodes() == Ethalon

    Tree.MoveNode(RightNodeB, LeftNode)
    MovedEthalon = [
        RootNode, LeftNode, RightNodeB, RightNodeB_1, RightNode, RightNodeA
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
    assert Tree.Count() == 1
    assert Tree.LeafCount() == 1

    LeftNode = SimpleTreeNode(7, None)
    Tree.AddChild(RootNode, LeftNode)
    assert Tree.Count() == 2
    assert Tree.LeafCount() == 1

    RightNode = SimpleTreeNode(21, None)
    Tree.AddChild(RootNode, RightNode)
    assert Tree.Count() == 3
    assert Tree.LeafCount() == 2

    RightNodeA = SimpleTreeNode(19, None)
    Tree.AddChild(RightNode, RightNodeA)
    assert Tree.Count() == 4
    assert Tree.LeafCount() == 2

    RightNodeB = SimpleTreeNode(23, None)
    Tree.AddChild(RightNode, RightNodeB)
    assert Tree.Count() == 5
    assert Tree.LeafCount() == 3

    RightNodeB_1 = SimpleTreeNode(15, None)
    Tree.AddChild(RightNodeB, RightNodeB_1)
    assert Tree.Count() == 6
    assert Tree.LeafCount() == 3


def test_event_tree():
    RootNode = SimpleTreeNode(1, None)
    Tree = SimpleTree(RootNode)

    A1_Node = SimpleTreeNode(2, RootNode)
    B1_A1_Node = SimpleTreeNode(5, A1_Node)
    B2_A1_Node = SimpleTreeNode(7, A1_Node)
    Tree.AddChild(RootNode, A1_Node)
    Tree.AddChild(A1_Node, B1_A1_Node)
    Tree.AddChild(A1_Node, B2_A1_Node)

    A2_Node = SimpleTreeNode(3, RootNode)
    B1_A2_Node = SimpleTreeNode(4, A2_Node)
    Tree.AddChild(RootNode, A2_Node)
    Tree.AddChild(A2_Node, B1_A2_Node)

    A3_Node = SimpleTreeNode(6, RootNode)
    B1_A3_Node = SimpleTreeNode(8, A3_Node)
    C1_B1_A3_Node = SimpleTreeNode(9, B1_A3_Node)
    C2_B1_A3_Node = SimpleTreeNode(10, B1_A3_Node)
    Tree.AddChild(RootNode, A3_Node)
    Tree.AddChild(A3_Node, B1_A3_Node)
    Tree.AddChild(B1_A3_Node, C1_B1_A3_Node)
    Tree.AddChild(B1_A3_Node, C2_B1_A3_Node)

    even = Tree.EvenTrees()
    print(Tree)
