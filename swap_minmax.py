"""Swap min max module"""
from typing import List


def swap_minmax(values: List[int]) -> List[int]:
    """Swap min max function"""
    if len(values) < 2:
        return values
    minimal, maximum = 0, 0
    minimal_index, maximum_index = 0, 0
    for index, value in enumerate(values):
        if index == 0:
            minimal = value
            maximum = value
            continue
        if value < minimal:
            minimal = value
            minimal_index = index
        if value > maximum:
            maximum = value
            maximum_index = index
    values[minimal_index], values[maximum_index] = values[maximum_index], values[minimal_index]
    return values
