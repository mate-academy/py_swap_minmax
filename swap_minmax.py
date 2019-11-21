"""docstring"""
from typing import List


def get_minmax(lis: List[int]) -> tuple:
    """
    Returns indexes of a minimal and maximal
    elements of a given list.
    """
    minimal = 0
    maximal = 0
    for idx, elem in enumerate(lis):
        if elem > maximal:
            maximal = idx
        elif elem < minimal:
            minimal = idx
    return minimal, maximal

def swap_minmax(lis: List[int]) -> List[int]:
    """Swaps minimal and maximal elements"""
    if len(lis) < 2:
        return lis

    mini, maxi = get_minmax(lis)
    lis[mini], lis[maxi] = lis[maxi], lis[mini]
    return lis
