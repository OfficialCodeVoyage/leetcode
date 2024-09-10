# Given a string with "?", return a palindrome if possible. EX: ?ab?b returns babab

strings_to_test = ["?ab??b", "a?b?a", "???", "a?c?b", "a??a", "a?b?c", "??a??", "a??b", "a?b?b?a", "a?b?c?d"]

def checkpol(string) -> str:
    answer_list = [i for i in string]

    if len(answer_list) % 2 != 0:
        return "Not a palindrome"

    l, r = 0, len(answer_list) - 1

    while l < r:
        if answer_list[l] == "?" and answer_list[r] == "?":
            answer_list[l] = "a"
            answer_list[r] = "a"
        elif answer_list[l] == "?":
            answer_list[l] = answer_list[r]
        elif answer_list[r] == "?":
            answer_list[r] = answer_list[l]

        l += 1
        r -= 1

    answer_string = ""

    for i in answer_list:
        answer_string += i

    return answer_string

for i in strings_to_test:
    print(checkpol(i))
