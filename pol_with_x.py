# Given a string with "?", return a palindrome if possible. EX: ?ab?b returns babab

string = "?ab??b"

def checkpol(string) -> str:
    answer_list = [i for i in string]

    if len(answer_list) % 2 != 0:
        return "Not a palindrome"

    l, r = 0, len(answer_list) - 1

    while l < r:
        if answer_list[l] == "?":
            answer_list[l] = answer_list[r]
        elif answer_list[r] == "?":
            answer_list[r] = answer_list[l]
        l += 1
        r -= 1

    answer_string = ""

    for i in answer_list:
        answer_string += i

    return answer_string

print(checkpol(string))