# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.


s = "A man, a plan, a canal: Panama"

def pol(string):
    ar = ''

    for i in string:
        if i.isalpha() or i.isnumeric():
            ar += i.lower()

    print(ar)

    po1, po2 = 0, len(ar) - 1

    while po1 < po2:
        if ar[po1] == ar[po2]:
            po1 += 1
            po2 -= 1
        else:
            return False
    return True


print(pol(s))