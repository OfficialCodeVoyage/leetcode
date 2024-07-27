# 88. Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
# the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate
# this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are
# set to 0 and should be ignored. nums2 has a length of n.
#

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#
#
#
#
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
#


# def sortedarr(nums1, nums2, m, n):
#     nums1 += nums2
#     nums1.sort(reverse=True)
#     number = m + n
#     nums3 = nums1[0:number]
#     nums1 = nums3
#     nums1.sort()
#     print(nums1)
#
#
#
# nums1, nums2, m, n = [1,2,3,0,0,0], [2,5,6], 3, 3
#
# sortedarr

# 123000
# 256

#
# def sorted(nums1, nums2, m, n):
#     pointer1 = m - 1
#     pointer2 = n - 1
#     pointer = m + n - 1
#
#     while pointer2 >= 0:
#         if nums2[pointer2] > nums1[pointer1]:
#             nums1[pointer] = nums2[pointer2]
#             pointer2 -= 1
#         elif nums1[pointer1] >= nums2[pointer2]:
#             nums1[pointer] = nums1[pointer1]
#             pointer1 -= 1
#         else:
#             nums1[pointer] = nums2[pointer2]
#             pointer2 -= 1
#         pointer -= 1
#
#     print(nums1)
#
#
# nums1, nums2, m, n = [1, 2, 3, 0, 0, 0], [2, 5, 6], 3, 3
#
# sorted(nums1, nums2, m, n)


### leetcode with class final solution

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m - 1
        pointer2 = n - 1
        pointer = m + n - 1

        while pointer2 >= 0:
            if nums2[pointer2] > nums1[pointer1] and pointer1 > 0:
                nums1[pointer] = nums2[pointer2]
                pointer2 -= 1
            elif nums1[pointer1] >= nums2[pointer2] and pointer1 >= 0:
                nums1[pointer] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[pointer] = nums2[pointer2]
                pointer2 -= 1
            pointer -= 1
