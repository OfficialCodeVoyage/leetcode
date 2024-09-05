# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

nums = [0,0,1,1,1,2,2,3,3,4]

# nums = [1,2]
def duplicate(nums):
    if len(nums) <= 1:
        return len(nums)

    po1 = 1

    for po2 in range(1, len(nums)):
        if nums[po2] != nums[po2 - 1]:
            nums[po1] = nums[po2]
            po1 += 1

    return po1


print(duplicate(nums))