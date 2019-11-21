"""
swap_minmax
"""
from typing import List


def swap_minmax(numbers: List[int]) -> List[int]:
    """
    function replace max number and min number by places
    :param numbers: [int]
    :return: [int]
    """
    if len(numbers) == 0:
        return []

    max_number = numbers[0]
    min_number = numbers[0]
    index_min = 0
    index_max = 0

    for i, number in enumerate(numbers):
        if number > max_number:
            max_number = number
            index_max = i
        else:
            min_number = number
            index_min = i

    numbers[index_max], numbers[index_min] = min_number, max_number

    return numbers
