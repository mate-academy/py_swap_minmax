"""
Swapping minimal and maximal elements of a list
"""

from typing import List


def swap_minmax(nums: List[int]) -> List[int]:
    """ Swapping elements of a list """
    if len(nums) <= 1:
        return nums

    min_num, max_num = find_minmax(nums)
    min_index = nums.index(min_num)
    max_index = nums.index(max_num)
    nums[min_index] = max_num
    nums[max_index] = min_num
    return nums


def find_minmax(nums):
    """ Func find min & max values """
    min_num = max_num = nums[0]
    for num in nums[1:]:
        if min_num > num:
            min_num = num
        if max_num < num:
            max_num = num
    return min_num, max_num
