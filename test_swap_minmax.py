"""
docstring
"""
import swap_minmax


def test_empty():
    """

    :return:
    """
    assert swap_minmax.swap_minmax([]) == []


def test_ordered():
    """

    :return:
    """
    assert swap_minmax.swap_minmax([1, 2, 3, 4, 5]) == [5, 2, 3, 4, 1]


def test_all_the_same():
    """

    :return:
    """
    assert swap_minmax.swap_minmax([1, 1, 1]) ==[1, 1, 1]


def test_one_item():
    """

    :return:
    """
    assert swap_minmax.swap_minmax([1]) == [1]


def test_negative():
    """

    :return:
    """
    assert swap_minmax.swap_minmax([1, 2, 3, -1]) == [1, 2, -1, 3]
