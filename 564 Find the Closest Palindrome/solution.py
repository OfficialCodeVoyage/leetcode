# Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.
#
# The closest is defined as the absolute difference minimized between two integers.
#
#
#
# Example 1:
#Input: n = "123"
#Output: "121"

# need to find 2 polindromes first
# return max(save(pol1, pol2))

n = '120' # output 121

def forward_cheking(x) -> int:

    while True :
        number_to_check = int(x) + 1
        number = [i for i in str(number_to_check)]
        po1, po2 = 0, len(number) - 1

        while po1 < po2:

            if number[po1] == number[po2]:
                po1 +=1
                po2 -=1
            else:
                number_to_check +=1
                number = [i for i in str(number_to_check)]
                po1, po2 = 0, len(number) - 1


        return number_to_check


def backward_cheking(x) -> int:

    while True :
        number_to_check = int(x) - 1
        number = [i for i in str(number_to_check)]
        po1, po2 = 0, len(number) - 1

        while po1 < po2:

            if number[po1] == number[po2]:
                po1 +=1
                po2 -=1
            else:
                number_to_check -=1
                number = [i for i in str(number_to_check)]
                po1, po2 = 0, len(number) - 1


        return number_to_check


def nearestPalindromic(n: str) -> str:
    if int(n) < 0:
        return '0'
    elif 0 < int(n) < 10:
        return str(int(n) - 1)
    elif int(n) == 10 or int(n) == 11:
        return '9'

    forward_palindrome = forward_cheking(n)
    backward_palindrome = backward_cheking(n)

    if abs(forward_palindrome - int(n)) == abs(int(n) - backward_palindrome):
        return str(min(forward_palindrome, backward_palindrome))
    elif abs(forward_palindrome - int(n)) < abs(int(n) - backward_palindrome):
        return str(forward_palindrome)
    else:
        return str(backward_palindrome)

nearestPalindromic(n)