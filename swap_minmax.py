"""Create a function for swapping minimal
and maximal elements of a list.
Don't use built-in min()/max() functions.
"""

from typing import List


def swap_minmax(nums: List[int]) -> List[int]:
    """General function"""
    if not nums:
        return []

    smallest = nums[0]
    biggest = 0

    for num in nums:
        if num < smallest:
            smallest = num
        elif num > biggest:
            biggest = num
    index_small = nums.index(smallest)
    index_big = nums.index(biggest)
    nums[index_small], nums[index_big] = biggest, smallest
    return nums
