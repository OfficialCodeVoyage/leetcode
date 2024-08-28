# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
#
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
#
# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:
#
# Input: nums = [1]
# Output: 1


nums = [4, 1, 2, 1, 2]


def checknums(nums) -> int:

    #dict style
    emtpy_dic = {}
    count = 0
    for i in nums:
        if i in emtpy_dic:
            emtpy_dic[i] += 1
        else:
            emtpy_dic[i] = 1
    # print(emtpy_dic)


    for k,v in emtpy_dic.items():
        if v == 1:
            return k


print(checknums(nums))
