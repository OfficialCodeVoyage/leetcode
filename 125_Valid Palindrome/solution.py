###A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
#
#
# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
#


s = "A man, a plan, a canal: Panama"

def palindrome(s):
    string = ''

    for i in s:
        if i.isalpha() or i.isnumeric():
            string += i.lower()


    left, right = 0, len(string) - 1

    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True



print(palindrome(s))