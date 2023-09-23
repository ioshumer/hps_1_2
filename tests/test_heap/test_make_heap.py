import pytest

from src.heap_7 import Heap


@pytest.mark.parametrize(
    ('array'),
    [
        (list(range(15))),
        [30, 40, 50],
        [30, 40, 50, 60],
        [30, 40, 50, 60, 70],
    ]
)
def test_make_heap(array):
    heap = Heap()
    heap.MakeHeap(array, 3)
