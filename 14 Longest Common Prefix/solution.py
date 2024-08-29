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
strs = ["flower", "flow", "flight"]


# strs = ["dog","racecar","car"]

def longest(strs) -> str:
    str_answer = ''
    po1 = 0
    lenght = len(strs)
    m = min(len(s) for s in strs)

    while po1 < m:
        store = ''
        for i in strs:
            if strs[i][po1] != strs[0][po1]:
                break
            else:
                str_answer += strs[i][po1]
        po1 += 1


print(longest(strs))
