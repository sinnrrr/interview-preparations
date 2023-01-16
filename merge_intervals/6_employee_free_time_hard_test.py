"""
Problem Challenge 3

Employee Free Time (hard)

For ‘K’ employees, we are given a list of intervals representing the working
hours of each employee. Our goal is to find out if there is a free interval
that is common to all employees. You can assume that each list of employee
working hours is sorted on the start time.

Example 1
Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
Output: [3,5]
Explanation: Both the employess are free between [3,5].

Example 2
Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
Output: [4,6], [8,9]
Explanation: All employess are free between [4,6] and [8,9].

Example 3
Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
Output: [5,7]
Explanation: All employess are free between [5,7].
"""


import pytest


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


def find_employee_free_time_failed(schedule: list[list[Interval]]):
    free_schedule = [[] for _ in range(len(schedule))]

    for employee_idx in range(len(schedule)):
        employee = schedule[employee_idx]

        for interval_idx in range(1, len(employee)):
            working_interval, prev_working_interval = (
                employee[interval_idx],
                employee[interval_idx - 1],
            )

            start = prev_working_interval.end
            end = working_interval.start

            free_schedule[employee_idx].append(Interval(start, end))


def find_employee_free_time(schedule: list[list[Interval]]):
    if len(schedule) == 0:
        return []

    flat_schedule: list[Interval] = []
    for employee in schedule:
        for working_interval in employee:
            flat_schedule.append(working_interval)

    flat_schedule.sort(key=lambda x: x.start)

    res = []
    latest_end = 1
    for working_interval in flat_schedule:
        if latest_end < working_interval.start:
            res.append(Interval(latest_end, working_interval.start))

        latest_end = max(latest_end, working_interval.end)

    return res


@pytest.mark.parametrize(
    "schedule, expected",
    [
        (
            [
                [Interval(1, 3), Interval(5, 6)],
                [
                    Interval(2, 3),
                    Interval(6, 8),
                ],
            ],
            [Interval(3, 5)],
        ),
        (
            [
                [Interval(1, 3), Interval(9, 12)],
                [Interval(2, 4)],
                [
                    Interval(6, 8),
                ],
            ],
            [Interval(4, 6), Interval(8, 9)],
        ),
        (
            [
                [Interval(1, 3)],
                [Interval(2, 4)],
                [
                    Interval(3, 5),
                    Interval(7, 9),
                ],
            ],
            [Interval(5, 7)],
        ),
    ],
)
def test_grokking(schedule, expected):
    assert find_employee_free_time(schedule) == expected
