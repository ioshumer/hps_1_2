import pytest

from src.heap_7 import Heap


def validate_heap(heap: Heap, idx: int | None = 0):
    if idx is None:
        return True
    LeftChildIdx = Heap.GetLeftChildIdx(idx)
    RightChildIdx = Heap.GetRightChildIdx(idx)


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
    print(heap.HeapArray)
