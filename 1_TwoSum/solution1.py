# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
from typing import Tuple, Any

nums = [2,7,11,15]
target = 9

def sum(nums, target) -> tuple[Any, Any]:

    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return i, j
    #
    #     return -1, -1

    dict = {}

    for i, n in enumerate(nums):
        complement = target - n
        if complement in dict:
            return dict[complement], i
        dict[n] = i

print(sum(nums, target))

