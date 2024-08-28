# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
#
#
#
# Example 1:
#
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.


nums = [3, 0, 1]

def missingnum(nums) -> int:

    list1 = []

    for i in range(0, len(nums)+1):
        list1.append(i)
    # print(list1)

    for i in list1:
        if i not in nums:
            return i


print(missingnum(nums))