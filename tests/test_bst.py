import pytest

from src.bst_1 import BSTNode, BST


@pytest.fixture()
def BinarySearchTree():
    """
    (25, "Hello")
        (15, "World")
            (7, "?")
            (17, "*")
        (32, "Amigo")
            (27, "!")
            (35, "...")

    :return:
    """
    Root = BSTNode(25, "Hello", None)
    Bst = BST(Root)

    Bst.AddKeyValue(15, "World")
    Bst.AddKeyValue(7, "?")
    Bst.AddKeyValue(17, "*")

    Bst.AddKeyValue(32, "Amigo")
    Bst.AddKeyValue(27, "!")
    Bst.AddKeyValue(35, "...")

    return Bst


def test_find(BinarySearchTree: BST):
    BSTFind_1 = BinarySearchTree.FindNodeByKey(7)
    assert BSTFind_1.Node.NodeValue == "?"
    assert BSTFind_1.NodeHasKey is True

    MissedLeftNode_A = BinarySearchTree.FindNodeByKey(1)
    assert MissedLeftNode_A.NodeHasKey is False
    assert MissedLeftNode_A.ToLeft is True
    assert MissedLeftNode_A.Node == BSTFind_1.Node

    MissedLeftNode_B = BinarySearchTree.FindNodeByKey(8)
    assert MissedLeftNode_B.NodeHasKey is False
    assert MissedLeftNode_B.ToLeft is False
    assert MissedLeftNode_B.Node == BSTFind_1.Node

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
    assert MinNode_1.NodeKey == 7
    MaxNode_1 = BinarySearchTree.FinMinMax(BinarySearchTree.Root, FindMax=True)
    assert MaxNode_1.NodeKey == 35

    FirstNodeResult = BinarySearchTree.FindNodeByKey(15)
    FirstNode = FirstNodeResult.Node

    MinNode_2 = BinarySearchTree.FinMinMax(FirstNode, FindMax=False)
    assert MinNode_2.NodeKey == 7
    MaxNode_2 = BinarySearchTree.FinMinMax(FirstNode, FindMax=True)
    assert MaxNode_2.NodeKey == 17


def test_del_by_key(BinarySearchTree: BST):
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


def test_count(BinarySearchTree: BST):
    assert BinarySearchTree.Count() == 7
