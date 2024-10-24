#Example 1:
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

x = 121



def polindrome(number) -> bool:
    if number < 0:
        return False
    elif 0 < number < 10:
        return False

    l_number = [i for i in str(number)]


    po1, po2 = 0, len(l_number) - 1

    while po1 < po2:
        if l_number[po1] == l_number[po2]:
            po1 +=1
            po2 -=1
        else:
            return False
    return True


print(polindrome(x))