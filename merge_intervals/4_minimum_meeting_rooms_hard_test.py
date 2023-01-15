"""
Solution Review: Problem Challenge 1 - Minimum Meeting Rooms (hard)
Given a list of intervals representing the start and end time of ‘N’ meetings,
find the minimum number of rooms required to hold all the meetings.

Example 1
Meetings: [[1,4], [2,5], [7,9]]
Output: 2
Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two
meetings. [7,9] can occur in any of the two rooms later.

Example 2
Meetings: [[6,7], [2,4], [8,12]]
Output: 1
Explanation: None of the meetings overlap, therefore we only need one room to
hold all meetings.

Example 3
Meetings: [[1,4], [2,3], [3,6]]
Output: 2
Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6],
we need two rooms to hold all the meetings.

Example 4
Meetings: [[4,5], [2,3], [2,4], [3,5]]
Output: 2
Explanation: We will need one room for [2,3] and [3,5], and another room for
[2,4] and [4,5].

My Example
Meetings: [[1,4], [2,4], [3,6]]
Output: 3
Explanation: We will need three rooms to hold meetings as all of them intercept
each other.
"""


def min_meeting_rooms(meetings: list[list[int]]) -> int:
    START, END = 0, 1
    meetings.sort(key=lambda x: x[START])

    rooms = [0]

    for meeting in meetings:
        i = 0
        while True:
            if i > len(rooms) - 1:
                rooms.append(0)

            if meeting[START] >= rooms[i]:
                rooms[i] = meeting[END]
                break

            i += 1

    return len(rooms)


def min_meeting_rooms_custom(meetings):
    rooms = [[]]  # the values are intervals at which they are busy
    for meeting in meetings:
        i = 0
        while True:
            # create new room if needed
            if i > len(rooms) - 1:
                rooms.append([])

            # insert meeting if not busy at the meeting time
            if len(interval_intersection(rooms[i], [meeting])) == 0:
                rooms[i].append(meeting)
                break

            i += 1

    return len(rooms)


# from question 2 (changed from `start <= end` to `start < end`)
# can be simplier since we don't need array as 2nd argument and interceptions
def interval_intersection(
    arr1: list[list[int]], arr2: list[list[int]]
) -> list[list[int]]:
    if arr1 == [] or arr2 == []:
        return []

    res = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        start = max(arr1[i][0], arr2[j][0])
        end = min(arr1[i][1], arr2[j][1])

        if start < end:
            res.append([start, end])

        if arr1[i][1] < arr2[j][1]:
            i += 1
        else:
            j += 1

    return res


def test_grokking():
    fn_arr = [min_meeting_rooms, min_meeting_rooms_custom]

    for fn in fn_arr:
        assert fn([[1, 4], [2, 5], [7, 9]]) == 2
        assert fn([[6, 7], [2, 4], [8, 12]]) == 1
        assert fn([[1, 4], [2, 3], [3, 6]]) == 2
        assert fn([[4, 5], [2, 3], [2, 4], [3, 5]]) == 2


def test_custom():
    fn_arr = [min_meeting_rooms_custom]

    for fn in fn_arr:
        assert fn([[1, 4], [2, 4], [3, 6]]) == 3
