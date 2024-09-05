# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
strs = ["flower", "flow", "floight"]


# strs = ["dog","racecar","car"]

def longest(strs) -> str:
    prefix = strs[0]  #flower
    answer = ""
    po1 = 0

    for i in prefix:
        for j in range(1, len(strs)):
            if po1 >= len(strs[j]) or i != strs[j][po1]:
                return answer
        answer += i
        po1 += 1

    return answer


print(longest(strs))
