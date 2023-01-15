"""
Given a list of intervals, merge all the overlapping intervals to produce a
list that has only mutually exclusive intervals.

Example 1
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged
them into one [1,5].

Example 2
Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into
one [5,9].

Example 3
Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.
"""


def merge_intervals(arr: list[list[int]]):
    arr.sort(key=lambda x: x[0])

    START, END = 0, 1
    n = len(arr)
    res, j = [arr[START]], 0
    for i in range(1, n):
        a, b = res[j], arr[i]

        if a[END] >= b[START]:
            res[j][END] = max(a[END], b[END])
            continue

        res.append(arr[i])
        j += 1

    return res


def test_grokking():
    assert merge_intervals([[1, 4], [2, 5], [7, 9]]) == [[1, 5], [7, 9]]
    assert merge_intervals([[6, 7], [2, 4], [5, 9]]) == [[2, 4], [5, 9]]
    assert merge_intervals([[1, 4], [2, 6], [3, 5]]) == [[1, 6]]
