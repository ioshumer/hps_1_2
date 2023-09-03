import pytest

from src.abst_4 import aBST


level_1 = [50]
level_2 = [50, 25, 75]
level_3 = [50, 25, 75, 13, 37, 63, 88]
level_4 = [50, 25, 75, 13, 37, 63, 88, 7, 20, 30, 45, 55, 70, 81, 95]


@pytest.fixture(scope="function")
def abst_level_0() -> aBST:
    aTree = aBST(0)
    return aTree


@pytest.fixture(scope="function")
def abst_level_1() -> aBST:
    aTree = aBST(1)
    aTree.Tree = level_1
    return aTree


@pytest.fixture(scope="function")
def abst_level_2() -> aBST:
    aTree = aBST(2)
    aTree.Tree = level_2
    return aTree


@pytest.fixture(scope="function")
def abst_level_3() -> aBST:
    aTree = aBST(3)
    aTree.Tree = level_3
    return aTree


@pytest.fixture(scope="function")
def abst_level_4() -> aBST:
    aTree = aBST(4)
    aTree.Tree = level_4
    return aTree
