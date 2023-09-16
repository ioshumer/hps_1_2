import pytest

from src.bbst_6 import BalancedBST


@pytest.fixture(scope="function")
def l0():
    return [50]


@pytest.fixture(scope="function")
def l1_f():
    return [25, 50, 75]


@pytest.fixture(scope="function")
def l1_p1():
    return [25, 50]


@pytest.fixture(scope="function")
def l2_f():
    return [13, 25, 37, 50, 63, 75, 88]


@pytest.fixture(scope="function")
def l2_p1():
    return [13, 25, 50, 63]


@pytest.fixture(scope="function")
def l2_p2():
    return [13, 25, 50, 63, 75]


@pytest.fixture(scope="function")
def l2_p3():
    return [13, 25, 50, 63, 75, 88]


@pytest.fixture(scope="function")
def empty_bbst():
    bbst = BalancedBST()
    return bbst
