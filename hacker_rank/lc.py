# ###1
# if __name__ == '__main__':
#     # x = int(input())
#     # y = int(input())
#     # z = int(input())
#     # n = int(input())
#
#     ## all cases
#     def all_cases(x=1, y=1, z=2) -> []:
#         all_cases = []
#
#         cases = [[i,j,k] for i in range(0,x+1) for j in range(0, y+1) for k in range(0,z+1)]
#         return cases
#
#
#     ## cases where it's not equal to n
#
#     def equal_cases(cases, n=3):
#         equal_cases = [i for i in cases if i[1]+i[2]+i[0]==n]
#
#
#         return equal_cases
#
#
#     # print(equal_cases(all_cases(x, y, z), 3))
#     print(equal_cases(all_cases()))

#2 second lowest


# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#
#
# ### need to print second lowest, if there are 2 grades print them alphabetically
#
# highest = students[0][1]
# runner = float('inf')
#
# for i in range(1, len(students)):
#     if students[i][1] < highest:
#         runner = highest
#         highest = students[i][1]
#     elif students[i][1] < runner and students[i][1] != highest:
#         runner = students[i][1]
#
# print(runner)
#
# selected = [i for i in range(0,len(students)) if students[i][1] == runner]
# ready = []
#
# for i in selected:
#     ready.append(students[i])
#
# ready.sort()
#
#
#
#

###3

string = 'Banana'
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']



def count_stuart(string):
    words = []

    for po1 in range(len(string)):
        if string[po1].lower() in consonants:
            for po2 in range(po1 + 1, len(string)+ 1):
                words.append(string[po1:po2])

    score_dict = {word : words.count(word) for word in words}
    total_points = 0

    for k,v in score_dict.items():
        total_points += v

    return total_points

def count_kevin(string):
    words = []

    for po1 in range(len(string)):
        if string[po1].lower() in vowels:
            for po2 in range(po1 + 1, len(string) + 1):
                words.append(string[po1:po2])

    score_dict = {word: words.count(word) for word in words}
    total_points = 0

    for k, v in score_dict.items():
        total_points += v

    return total_points

def minion_game(string) -> str:
    kevin = count_kevin(string)
    stuart = count_stuart(string)
    result = ''
    if kevin > stuart:
        result = f'Kevin {kevin}'
    elif stuart > kevin:
        result = f'Stuart {stuart}'
    else:
        result = 'Draw'

    return result


print(minion_game(string))





















