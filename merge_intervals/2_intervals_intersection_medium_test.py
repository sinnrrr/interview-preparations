"""
Given two lists of intervals, find the intersection of these two lists.
Each list consists of disjoint intervals sorted on their start time.

Example 1
Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between
the two lists.

Example 2
Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between
the two lists.

https://leetcode.com/problems/interval-list-intersections/solutions/1594098/python-two-pointers-solution/?orderBy=most_votes&languageTags=python3
"""


def interval_intersection(
    arr1: list[list[int]], arr2: list[list[int]]
) -> list[list[int]]:
    if not arr1:
        return []

    res = []
    i, j = 0, 0
    START, END = 0, 1

    while i < len(arr1) and j < len(arr2):
        a, b = arr1[i], arr2[j]

        if b[START] > a[END]:
            i += 1
            continue

        if b[END] < a[START]:
            j += 1
            continue

        start = max(a[START], b[START])
        if b[END] <= a[END]:
            end = b[END]
            res.append([start, end])
            j += 1
            continue

        end = a[END]
        res.append([start, end])
        i += 1

    return res


# leetcode more elegant solution
def intervalIntersection(
    arr1: list[list[int]], arr2: list[list[int]]
) -> list[list[int]]:
    if arr1 == [] or arr2 == []:
        return []

    res = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        start = max(arr1[i][0], arr2[j][0])
        end = min(arr1[i][1], arr2[j][1])

        if start <= end:
            res.append([start, end])

        if arr1[i][1] < arr2[j][1]:
            i += 1
        else:
            j += 1

    return res


def test_grokking():
    fn = interval_intersection

    assert fn([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]) == [
        [2, 3],
        [5, 6],
        [7, 7],
    ]

    assert fn([[1, 3], [5, 7], [9, 12]], [[5, 10]]) == [
        [5, 7],
        [9, 10],
    ]


def test_leetcode():
    fn = interval_intersection

    assert fn(
        [[1, 5], [8, 12], [15, 24], [25, 26]],
        [[0, 2], [5, 10], [13, 23], [24, 25]],
    ) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

    assert fn([], [[1, 3], [5, 9]]) == []

    # submit
    assert fn([[5, 6]], [[5, 10]]) == [[5, 6]]
    assert fn([[2, 11], [12, 13]], [[1, 8], [16, 20]]) == [[2, 8]]
    assert fn([[1, 6], [8, 11], [13, 17], [19, 20]], [[10, 12], [18, 19]]) == [
        [10, 11],
        [19, 19],
    ]
