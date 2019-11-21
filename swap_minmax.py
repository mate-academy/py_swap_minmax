'''Module'''
from typing import List


def swap(array, minimal_elem, max_elem):
    '''

    :param array:
    :param minimal_elem:
    :param max_elem:
    :return:
    '''

    min_e = array.index(minimal_elem)
    max_e = array.index(max_elem)
    array[min_e], array[max_e] = array[max_e], array[min_e]
    return array


def find_min_max(array):
    '''

    :param array:
    :return:
    '''
    minimal_element = array[0]
    maxmal_element = array[0]
    for i in array:
        if i < minimal_element:
            minimal_element = i
        else:
            maxmal_element = i
    return (minimal_element, maxmal_element)


def swap_minmax(nabir: List[int]) -> List[int]:
    '''

    :param nabir:
    :return:
    '''
    if len(nabir) == 0:
        return nabir
    minimal_elem, max_elem = find_min_max(nabir)
    nabir = swap(nabir, minimal_elem, max_elem)
    print(nabir)
    return nabir
