"""
docstring
"""


def swap_minmax(lst):
    """

    :param lst:
    :return:
    """
    if len(lst) < 2:
        return lst
    new_l = sorted(lst)
    max_index = lst.index(new_l[-1])
    min_index = lst.index(new_l[0])
    lst[max_index], lst[min_index] = lst[min_index], lst[max_index]
    return lst
