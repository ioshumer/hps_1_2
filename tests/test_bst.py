import pytest

from src.bst_1 import BSTNode, BST


@pytest.fixture()
def BinarySearchTree():
    """
    (25, "Hello")
        (15, "World")
            (7, "?")
                (4, "=")
                (10, "-")
            (17, "*")
                (16, "&")
                (20, "#")
        (32, "Amigo")
            (27, "!")
            (35, "...")
    """
    Root = BSTNode(25, "Hello", None)
    Bst = BST(Root)

    Bst.AddKeyValue(15, "World")
    Bst.AddKeyValue(7, "?")
    Bst.AddKeyValue(17, "*")

    Bst.AddKeyValue(4, "=")
    Bst.AddKeyValue(10, "-")

    Bst.AddKeyValue(16, "&")
    Bst.AddKeyValue(20, "#")

    Bst.AddKeyValue(32, "Amigo")
    Bst.AddKeyValue(27, "!")
    Bst.AddKeyValue(35, "...")

    return Bst


def test_add_node(BinarySearchTree: BST):
    RootNode = BinarySearchTree.FindNodeByKey(25).Node
    assert RootNode.NodeKey == 25

    LeftChild_1 = RootNode.LeftChild
    RightChild_1 = RootNode.RightChild
    assert LeftChild_1.NodeKey == 15
    assert RightChild_1.NodeKey == 32

    LeftChild_1_1 = LeftChild_1.LeftChild
    RightChild_1_1 = LeftChild_1.RightChild
    assert LeftChild_1_1.NodeKey == 7
    assert RightChild_1_1.NodeKey == 17

    LeftChild_1_2 = RightChild_1.LeftChild
    RightChild_1_2 = RightChild_1.RightChild
    assert LeftChild_1_2.NodeKey == 27
    assert RightChild_1_2.NodeKey == 35

    LeftChild_1_1_1 = LeftChild_1_1.LeftChild
    RightChild_1_1_1 = LeftChild_1_1.RightChild
    assert LeftChild_1_1_1.NodeKey == 4
    assert RightChild_1_1_1.NodeKey == 10

    LeftChild_1_2_1 = RightChild_1_1.LeftChild
    RightChild_1_2_1 = RightChild_1_1.RightChild
    assert LeftChild_1_2_1.NodeKey == 16
    assert RightChild_1_2_1.NodeKey == 20


def test_find(BinarySearchTree: BST):
    BSTFind_1 = BinarySearchTree.FindNodeByKey(4)
    assert BSTFind_1.Node.NodeValue == "="
    assert BSTFind_1.NodeHasKey is True

    BSTFind_1_1 = BinarySearchTree.FindNodeByKey(10)
    assert BSTFind_1_1.NodeHasKey is True

    MissedLeftNode_A = BinarySearchTree.FindNodeByKey(1)
    assert MissedLeftNode_A.NodeHasKey is False
    assert MissedLeftNode_A.ToLeft is True
    assert MissedLeftNode_A.Node == BSTFind_1.Node

    MissedLeftNode_B = BinarySearchTree.FindNodeByKey(8)
    assert MissedLeftNode_B.NodeHasKey is False
    assert MissedLeftNode_B.ToLeft is True
    assert MissedLeftNode_B.Node == BSTFind_1_1.Node

    BSTFind_2 = BinarySearchTree.FindNodeByKey(35)
    assert BSTFind_2.Node.NodeValue == "..."
    assert BSTFind_2.NodeHasKey is True

    MissedRightNode_A = BinarySearchTree.FindNodeByKey(33)
    assert MissedRightNode_A.NodeHasKey is False
    assert MissedRightNode_A.ToLeft is True
    assert MissedRightNode_A.Node == BSTFind_2.Node

    MissedRightNode_B = BinarySearchTree.FindNodeByKey(37)
    assert MissedRightNode_B.NodeHasKey is False
    assert MissedRightNode_B.ToLeft is False
    assert MissedRightNode_B.Node == BSTFind_2.Node


def test_add(BinarySearchTree: BST):
    ExistingKey = 35
    NewValue = "$"
    assert BinarySearchTree.AddKeyValue(ExistingKey, NewValue) is False
    BSTFind = BinarySearchTree.FindNodeByKey(ExistingKey)
    assert BSTFind.Node.NodeValue != NewValue


def test_find_mix_max(BinarySearchTree: BST):
    MinNode_1 = BinarySearchTree.FinMinMax(BinarySearchTree.Root, FindMax=False)
    assert MinNode_1.NodeKey == 4
    MaxNode_1 = BinarySearchTree.FinMinMax(BinarySearchTree.Root, FindMax=True)
    assert MaxNode_1.NodeKey == 35

    FirstNodeResult = BinarySearchTree.FindNodeByKey(15)
    FirstNode = FirstNodeResult.Node

    MinNode_2 = BinarySearchTree.FinMinMax(FirstNode, FindMax=False)
    assert MinNode_2.NodeKey == 4
    MaxNode_2 = BinarySearchTree.FinMinMax(FirstNode, FindMax=True)
    assert MaxNode_2.NodeKey == 20


def test_simple_del_by_key(BinarySearchTree: BST):
    NonExistedKey = 33
    result = BinarySearchTree.DeleteNodeByKey(NonExistedKey)
    assert result is False

    BinarySearchTree.AddKeyValue(18, ",")
    FindedNode = BinarySearchTree.FindNodeByKey(18)
    assert FindedNode.NodeHasKey is True

    BinarySearchTree.DeleteNodeByKey(18)
    AgainFindedNode = BinarySearchTree.FindNodeByKey(18)
    assert AgainFindedNode.NodeHasKey is False

    BinarySearchTree.AddKeyValue(18, ",")
    AddedNodeResult = BinarySearchTree.FindNodeByKey(18)
    AddedNode = AddedNodeResult.Node
    assert AddedNodeResult.ToLeft is False

    print('*' * 33)
    print(AddedNode)

    FindedNodeResult_A = BinarySearchTree.FindNodeByKey(15)
    FindedNode_A = FindedNodeResult_A.Node
    BinarySearchTree.DeleteNodeByKey(17)
    assert AddedNode.Parent == FindedNode_A


def test_del_by_key(BinarySearchTree: BST):
    """
    (25, "Hello")
        (15, "World")
            (7, "?")
                (4, "=")
                (10, "-")
            (17, "*")
                (16, "&")
                (20, "#")
        (32, "Amigo")
            (27, "!")
            (35, "...")

    (25, "Hello")
        (16, "&")
            (7, "?")
                (4, "=")
                (10, "-")
            (17, "*")
                ()
                (20, "#")
        (32, "Amigo")
            (27, "!")
            (35, "...")
    """
    BinarySearchTree.DeleteNodeByKey(15)
    print(BinarySearchTree)

    RootNode = BinarySearchTree.FindNodeByKey(25).Node
    assert RootNode.NodeKey == 25

    LeftChild_1 = RootNode.LeftChild
    RightChild_1 = RootNode.RightChild
    assert LeftChild_1.NodeKey == 16
    assert RightChild_1.NodeKey == 32

    LeftChild_1_1 = LeftChild_1.LeftChild
    RightChild_1_1 = LeftChild_1.RightChild
    assert LeftChild_1_1.NodeKey == 7
    assert RightChild_1_1.NodeKey == 17

    LeftChild_1_2 = RightChild_1.LeftChild
    RightChild_1_2 = RightChild_1.RightChild
    assert LeftChild_1_2.NodeKey == 27
    assert RightChild_1_2.NodeKey == 35

    LeftChild_1_1_1 = LeftChild_1_1.LeftChild
    RightChild_1_1_1 = LeftChild_1_1.RightChild
    assert LeftChild_1_1_1.NodeKey == 4
    assert RightChild_1_1_1.NodeKey == 10

    LeftChild_1_2_1 = RightChild_1_1.LeftChild
    RightChild_1_2_1 = RightChild_1_1.RightChild
    assert LeftChild_1_2_1 is None
    assert RightChild_1_2_1.NodeKey == 20


def test_count(BinarySearchTree: BST):
    assert BinarySearchTree.Count() == 11
