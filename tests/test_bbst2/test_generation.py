import pytest


@pytest.mark.parametrize(
    ('array', 'depth'),
    [
        ([50], 0),
        ([25, 50, 75], 1),
        ([25, 50], 1),
        ([13, 25, 37, 50, 63, 75, 88], 2),
        ([13, 25, 50, 63], 2),
        ([13, 25, 50, 63, 75], 2),
        ([13, 25, 50, 63, 75, 88], 2),
        ([13, 25, 50, 63, 75, 88], 2),
        ([50, 25, 75, 13, 37, 63, 88, 7, 20, 30, 45, 55, 70, 81, 95], 3)
    ]
)
def test_max_depth_and_balance(array, depth, bbst):
    bbst.GenerateTree(array)

    assert bbst._GetDepthOfSubtree(bbst.Root) == depth

    LeftChild = bbst.Root.LeftChild
    RightChild = bbst.Root.RightChild

    if LeftChild is not None:
        LeftChildDepth = bbst._GetDepthOfSubtree(LeftChild)
    else:
        LeftChildDepth = 0

    if RightChild is not None:
        RightChildDepth = bbst._GetDepthOfSubtree(RightChild)
    else:
        RightChildDepth = 0

    assert abs(LeftChildDepth - RightChildDepth) <= 1


def test_bbst(filled_bbst):
    assert filled_bbst.IsBalanced(filled_bbst.Root)
