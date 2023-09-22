import pytest

from src.heap_7 import Heap


@pytest.mark.parametrize(
    ('array'),
    [
        (list(range(15))),

    ]
)
def test_make_heap(array):
    heap = Heap()
    heap.MakeHeap(array, 3)
    print(heap.HeapArray)