# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some
# (can be none) of the characters without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#
#
#
# Example 1:
#
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
#
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
s, t = "bb", "ahbgcd"


def check(s, t) -> bool:
    list1 = [i for i in s] # b b
    list2 = [i for i in t] # a h b g c d

    po1, po2 = 0, 0
    stop = list2[-1]

    if len(list1) == 0:
        return False

    while po1 < len(list1):
        if list1[po1] == list2[po2]:
            po1 += 1

        elif list2[po2] == stop:
            return False
        po2 += 1

    return True




print(check(s, t))
