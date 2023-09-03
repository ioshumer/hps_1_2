from src.abst_4 import aBST


def test_add_empty_tree(abst_level_0: aBST):
    index = abst_level_0.AddKey(0)
    assert index == 0
    assert len(abst_level_0) == 1
    assert abst_level_0.Tree == [0]
