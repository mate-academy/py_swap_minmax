"""swap min and max value in list"""
from typing import List


def get_max_value_from_list(lst):
    """takes list and returns max value"""
    _max_val = lst[0]
    for num in lst:
        if _max_val < num:
            _max_val = num
    return _max_val


def get_min_value_from_list(lst):
    """takes list and returns min value"""
    _min_value = lst[0]
    for num in lst:
        if num < _min_value:
            _min_value = num
    return _min_value


def swap_minmax(numbers_list: List[int]) -> List[int]:
    """swaps min and max value in list and returns swapped list"""
    if numbers_list and not None:
        max_value = get_max_value_from_list(numbers_list)
        min_value = get_min_value_from_list(numbers_list)
        idx_min = [i for i, e in enumerate(numbers_list) if e == min_value]
        idx_max = [i for i, e in enumerate(numbers_list) if e == max_value]

        for idx in idx_min:
            numbers_list[idx] = max_value
        for idx in idx_max:
            numbers_list[idx] = min_value
    return numbers_list
