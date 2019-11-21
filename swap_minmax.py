"""docstring"""
from typing import List


def swap_minmax(arr: List[int]) -> List[int]:
    """swaps minimal and maximal values in list"""
    # noting to do with empty or short list
    if not arr:
        return arr
    if len(arr) < 2:
        return arr
    # compare every element with current min and max
    minimal = maximal = arr[0]
    for element in arr:
        if element > maximal:
            maximal = element
        if element < minimal:
            minimal = element
    # get position of min and max
    index_min = arr.index(minimal)
    index_max = arr.index(maximal)
    # swap min and max
    arr[index_min], arr[index_max] = arr[index_max], arr[index_min]

    return arr
