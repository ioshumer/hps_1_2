import pytest

from src.heap_7 import Heap


@pytest.mark.parametrize(
    ('initial_array', 'new_array', 'max_elem'),
    [
        ([], [None] * 7, -1),
        ([30], [None] * 7, 30),
        ([30, 40], [30] + [None] * 6, 40),
        ([30, 40, 50], [40, 30] + [None] * 5, 50),
        ([30, 40, 50, 60], [50, 30, 40] + [None] * 4, 60),
        ([30, 40, 50, 60, 70], [60, 50, 40, 30] + [None] * 3, 70),
    ]
)
def test_make_heap(initial_array, new_array, max_elem):
    heap = Heap()
    heap.MakeHeap(initial_array, 2)
    MaxElem = heap.GetMax()
    assert heap.HeapArray == new_array
    assert MaxElem == max_elem
