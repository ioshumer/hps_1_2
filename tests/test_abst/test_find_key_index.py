import pytest
from pytest_lazyfixture import lazy_fixture

from src.abst_4 import aBST


@pytest.mark.parametrize(
    "BinaryTree",
    [
        (lazy_fixture("abst_level_1")),
        (lazy_fixture("abst_level_2")),
        (lazy_fixture("abst_level_3")),
        (lazy_fixture("abst_level_4")),
    ]
)
def test_find_nonexisted_key(BinaryTree: aBST):
    NonExistedKey = 512
    SearchResult = BinaryTree.FindKeyIndex(NonExistedKey)
    assert SearchResult is None


@pytest.mark.parametrize(
    "BinaryTree",
    [
        (lazy_fixture("abst_level_1")),
        (lazy_fixture("abst_level_2")),
        (lazy_fixture("abst_level_3")),
        (lazy_fixture("abst_level_4")),
    ]
)
def test_find_first_existed(BinaryTree: aBST):
    ...
