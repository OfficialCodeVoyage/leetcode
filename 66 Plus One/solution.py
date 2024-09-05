# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.
#
#
#
# Example 1:
#
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

digits = [9, 9, 9]


def plusone(digits) -> []:
    # st = ""
    # for i in digits:
    #     st += str(i)
    # answer = int(st) + 1
    # answer1 = [int(i) for i in str(answer)]
    # return answer1

    digits.reverse()

    one, i = 1, 0

    while one:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                one = 0

        else:
            digits.append(1)
            one = 0

        i += 1

    return digits[::-1]

print(plusone(digits))
