"""
Problem Statement
Given an array of intervals representing ‘N’ appointments, find out
if a person can attend all the appointments.

Example 1
Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of
these appointments.

Example 2
Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend
all of them.

Example 3
Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of
these appointments.
"""


def can_attend_all_appointments(intervals):
    intervals.sort(key=lambda x: x[0])

    START, END = 0, 1

    last = intervals[0]
    for i in range(1, len(intervals)):
        start = max(last[START], intervals[i][START])
        end = min(last[END], intervals[i][END])

        if start <= end:
            return False

    return True


def test_grokking():
    fn = can_attend_all_appointments

    assert not fn([[1, 4], [2, 5], [7, 9]])
    assert fn([[6, 7], [2, 4], [8, 12]])
    assert not fn([[4, 5], [2, 3], [3, 6]])
