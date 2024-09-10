# Given an array of integers nums, calculate the pivot index of this array.
#
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
#
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
#
# Return the leftmost pivot index. If no such index exists, return -1.


nums = [1,7,3,6,5,6]

def pivot(nums) -> int:
    l, r = 0, len(nums) - 1
    l1, r1 = nums[l], nums[r]

    while l < r:
        if l1 < r1:
            l += 1
            l1 += nums[l]
        else:
            r -= 1
            r1 += nums[r]


    if l1 == r1:
        return l

    return -1


print(pivot(nums))