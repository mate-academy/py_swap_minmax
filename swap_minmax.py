"""
swap min/max module
"""

from typing import List


def get_position_min_num(lst: List[int]) -> int:
    """
    Return position index of minimum number from list.
    :param lst: List[int]
    :return: int
    """
    min_num = lst[0]
    min_num_idx = 0
    for idx, num in enumerate(lst):
        if lst[idx] < min_num:
            min_num_idx = idx
    return min_num_idx


def get_position_max_num(lst: List[int]) -> int:
    """
    Return position index of maximum number from list.
    :param lst: List[int]
    :return: int
    """
    max_num = lst[0]
    max_num_idx = 0
    for idx, num in enumerate(lst):
        if lst[idx] > max_num:
            max_num_idx = idx
    return max_num_idx


def swap_minmax(lst: List[int]) -> List[int]:
    """
    Swapping minimal and maximal elements of a list.
    :param lst: List[int]
    :return: List[int]
    """
    if len(lst) > 0:
        min_num_idx = get_position_min_num(lst)
        max_num_idx = get_position_max_num(lst)
    else:
        return lst
    min_max_nums = lst[min_num_idx], lst[max_num_idx]
    lst[max_num_idx], lst[min_num_idx] = min_max_nums
    return lst
