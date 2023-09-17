import pytest


@pytest.mark.parametrize(
    ('array', 'expected_idx'),
    [
        ([50], 0),
        ([25, 50, 75], 1),
        ([25, 50], 1),
        ([13, 25, 37, 50, 63, 75, 88], 3),
        ([13, 25, 50, 63], 2),
        ([13, 25, 50, 63, 75], 2),
        ([13, 25, 50, 63, 75, 88], 3),
    ]
)
def test_vertex_calculation(array, expected_idx, bbst):
    left_bound = 0
    right_bound = len(array) - 1
    assert bbst._DefineVertexIndex(left_bound, right_bound) == expected_idx
