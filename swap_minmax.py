"""please explain when do we really need this docstring"""
#from typing import List

def swap_minmax(initial_sequence):
    """docstring"""
    if len(initial_sequence) <= 1:
        return initial_sequence
    numbers_sequence = initial_sequence
    min_number = numbers_sequence[0]
    index_min = 0
    max_number = numbers_sequence[0]
    index_max = 0
    for number in numbers_sequence:
        if number > max_number:
            max_number = number
            index_max = numbers_sequence.index(number)
        if number < min_number:
            min_number = number
            index_min = numbers_sequence.index(number)
    numbers_sequence[index_max] = "swap to min_number"
    numbers_sequence[index_min] = "swap to max_number"
    for seq, value in enumerate(numbers_sequence):
        if value == "swap to min_number":
            numbers_sequence[seq] = min_number
        elif value == "swap to max_number":
            numbers_sequence[seq] = max_number

    return numbers_sequence
