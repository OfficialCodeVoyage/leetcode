# Input: n = 5, arr[] = [1,2,3,5]
# Output: 4
# Explanation : All the numbers from 1 to 5 are present except 4.


n = 2
ar = [1]

def check_miss(n, ar) -> int:
    correct_arr = [i for i in range(1, n+1)]
    missing = 0

    for i in correct_arr:
        if i not in ar:
            missing = i

    if missing != 0:
        return missing
    else:
        return "All good"


print(check_miss(n, ar))