""" swap minmax"""

from typing import List


def swap_minmax(list_fo_swap: List[int]) -> List[int]:
    """ return swap list"""
    min_value = 10
    max_value = 0
    min_position = 0
    max_position = 0
    lengths_list = len(list_fo_swap)
    if list_fo_swap:
        for i in range(lengths_list):
            if list_fo_swap[i] < min_value:
                min_value = list_fo_swap[i]
                min_position = i
            if list_fo_swap[i] > max_value:
                max_value = list_fo_swap[i]
                max_position = i
        list_fo_swap[min_position], list_fo_swap[max_position] =\
            list_fo_swap[max_position], list_fo_swap[min_position]

    return list_fo_swap
