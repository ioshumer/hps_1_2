import pytest
from pytest_lazyfixture import lazy_fixture

from src.abst_4 import aBST
from tests.test_abst.conftest import level_1, level_2, level_3, level_4


@pytest.mark.parametrize(
    ('binary_tree', 'tree_array'),
    [
        (lazy_fixture("abst_level_1"), level_1),
        (lazy_fixture("abst_level_2"), level_2),
        (lazy_fixture("abst_level_3"), level_3),
        (lazy_fixture("abst_level_4"), level_4),
    ]
)
def test_finding_keys(binary_tree, tree_array):
    for idx, value in enumerate(tree_array):
        assert binary_tree.FindKeyIndex(value) == idx


@pytest.mark.parametrize(
    "BinaryTree",
    [
        (lazy_fixture("abst_level_1")),
        (lazy_fixture("abst_level_2")),
        (lazy_fixture("abst_level_3")),
        (lazy_fixture("abst_level_4")),
    ]
)
def test_tree_balance(BinaryTree: aBST):
    for idx in range(len(BinaryTree)):
        CurrentKey = BinaryTree[idx]
        if CurrentKey is None:
            continue

        LeftChildIdx = BinaryTree.GetLeftChildIdx(idx)
        RightChildIdx = BinaryTree.GetRightChildIdx(idx)

        if LeftChildIdx >= len(BinaryTree) or RightChildIdx >= len(BinaryTree):
            break

        LeftChildKey = BinaryTree[LeftChildIdx]
        RightChildKey = BinaryTree[RightChildIdx]

        assert CurrentKey > LeftChildKey
        assert CurrentKey < RightChildKey



