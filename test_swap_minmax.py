import swap_minmax


def test_empty():
    assert swap_minmax.swap_minmax([]) == []


def test_ordered():
    assert swap_minmax.swap_minmax([1, 2, 3, 4, 5]) == [5, 2, 3, 4, 1]


def test_all_the_same():
    assert swap_minmax.swap_minmax([1, 1, 1]) == [1, 1, 1]


def test_one_item():
    assert swap_minmax.swap_minmax([1]) == [1]


def test_negative():
    assert swap_minmax.swap_minmax([1, 2, 3, -1]) == [1, 2, -1, 3]