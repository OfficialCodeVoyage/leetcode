#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

intervals = [[1,4],[2,3]]


def merge(intervals) -> list:
    answer = []
    sorted_int = sorted(intervals)

    for i in sorted_int:
        if not answer:
            answer.append(i)

        if answer[-1][1] >= i[0]:
            answer[-1] = [answer[-1][0], max(answer[-1][1], i[1])]
        else:
            answer.append(i)

    return answer


print(merge(intervals))