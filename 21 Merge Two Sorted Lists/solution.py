# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#  Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#

list1, list2 = [1, 2, 4], [1, 3, 4]


def merge2list(list1, list2) -> list:
    final_list = []
    po1, po2 = 0, 0
    itter = 0
    lenght = (len(list1) + len(list2))

    while itter < lenght:
        if po1 == len(list1):
            final_list.append(list2[po2])
            po2 += 1
            itter += 1
        elif po2 == len(list2):
            final_list.append(list1[po1])
            po1 += 1
            itter += 1

        elif list1[po1] <= list2[po2]:
            final_list.append(list1[po1])
            po1 += 1
            itter += 1
        else:
            if list1[po1] > list2[po2]:
                final_list.append(list2[po2])
                po2 += 1
                itter += 1

    return final_list


print(merge2list(list1, list2))
