#Given an integer x, return true if x is a
# palindrome
# , and false otherwise.
# Example 1:
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#

x = 121


def a(number) -> bool:
    linum = [i for i in str(number)]

    left, right = 0, len(linum) - 1

    while left < right:
        if linum[left] == linum[right]:
            left += 1
            right -= 1

        else:
            return False

    return True


print(a(x))
