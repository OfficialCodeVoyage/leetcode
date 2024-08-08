# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.


nums = [-1,0,1,2,-1,-4]

def threesum(nums):
    # for i in nums:
    #     for j in nums:
    #         for k in nums:
    #             if i + j + k == 0:
    #                 print(f"{i} + {j} + {k} = 0")#
    # brute force for fun
    #
    # dic_nums = {}
    # for i, v in enumerate(nums):
    #     dic_nums[i] = v
    #
    #
    # po1, po2 = 0, 1
    #
    #
    # while po2 < len(nums) -1:
    #     # if nums[left] + nums[right] == dic -value == 0
    #     iter = nums[po1] + nums[po2]
    #     listofsums = []
    #
    #     for k, v in dic_nums.items():
    #         if iter + v == 0:
    #             listofsums.append([nums[po1], nums[po2], nums[k]])
    #
    #     po1 += 1
    #     po2 += 1
    #
    # return listofsums

    nums.sort()
    i = 0
    left, right = i+1, len(nums)-1
    arr = []

    # while i < len(nums) - 2:
    #     if nums[i] + nums[left] + nums[right] == 0:
    #         res = [nums[i], nums[left], nums[right]]
    #         arr.append(res)
    #     i += 1
    #     left += 1
    #     right -= 1

    for i in nums:
        for j in nums:
                if nums[i] + nums[left] + nums[right] == 0:
                    res = [nums[i], nums[left], nums[right]]
                    arr.append(res)
                    i += 1
                    left += 1
                    right -= 1






    return arr







print(threesum(nums))