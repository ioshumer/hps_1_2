import pytest

from src.heap_7 import Heap


@pytest.mark.parametrize(
    ('array', 'tested_idx', 'expected_parent_idx', 'expected_left_idx', 'expected_right_idx'),
    [
        (list(range(15, 0, -1)), 0, None, 1, 2),
        (list(range(15, 0, -1)), 1, 0, 3, 4),
        (list(range(15, 0, -1)), 14, 6, None, None),

    ]
)
def test_max_depth_and_balance(array, tested_idx, expected_parent_idx, expected_left_idx, expected_right_idx):
    heap = Heap()
    heap.HeapArray = array
    assert heap.GetParentIdx(tested_idx) == expected_parent_idx
    assert heap.GetLeftChildIdx(tested_idx) == expected_left_idx
    assert heap.GetRightChildIdx(tested_idx) == expected_right_idx
