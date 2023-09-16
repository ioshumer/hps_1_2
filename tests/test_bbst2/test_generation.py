import pytest


@pytest.mark.parametrize(
    ('array'),
    [
        # ([50]),
        # ([25, 50, 75]),
        # ([25, 50]),
        # ([13, 25, 37, 50, 63, 75, 88]),
        ([13, 25, 50, 63]),
        # ([13, 25, 50, 63, 75]),
        # ([13, 25, 50, 63, 75, 88]),
    ]
)
def test_vertex_calculation(array, empty_bbst):
    print()
    tree = empty_bbst.GenerateTree(array)
    print()
