"""
Given a set of investment projects with their respective profits, we need to find the
most profitable projects. We are given an initial capital and are allowed to invest only
in a fixed number of projects. Our goal is to choose projects that give us the maximum
profit. Write a function that returns the maximum total capital after selecting the most
profitable projects.

We can start an investment project only when we have the required capital. Once a
project is selected, we can assume that its profit has become our capital.

Example 1:
Input: Project Capitals=[0,1,2], Project Profits=[1,2,3], Initial Capital=1,
Number of Projects=2
Output: 6
Explanation:
1. With initial capital of ‘1’, we will start the second project which will give us
profit of ‘2’. Once we selected our first project, our total capital will become 3
(profit + initial capital).
2. With ‘3’ capital, we will select the third project, which will give us ‘3’ profit.
After the completion of the two projects, our total capital will be 6 (1+2+3).

Example 2:
Input: Project Capitals=[0,1,2,3], Project Profits=[1,2,3,5], Initial Capital=0,
Number of Projects=3
Output: 8
Explanation:
1. With ‘0’ capital, we can only select the first project, bringing out capital to 1.
2. Next, we will select the second project, which will bring our capital to 3.
3. Next, we will select the fourth project, giving us a profit of 5.
After selecting the three projects, our total capital will be 8 (1+2+5).

https://leetcode.com/problems/ipo/solutions/3219920/heap-greedy-solution-beats-99-69-python-3
"""


from heapq import heappop, heappush

import pytest


def smart_invest_custom(
    capitals: list[int], profits: list[int], capital: int, nproj: int
) -> int:
    projects = list(zip(capitals, profits))

    while len(projects) > 0 and nproj > 0:
        projects_count = len(projects)
        available_proj_id, curr = None, 0
        while curr < projects_count:
            if projects[curr][0] > capital:
                available_proj_id = curr - 1
                break
            curr += 1
        if available_proj_id == -1:
            break
        if available_proj_id is None:
            available_proj_id = projects_count - 1

        available_proj = projects[available_proj_id]
        del projects[available_proj_id]

        capital += available_proj[1]
        nproj -= 1

    return capital


def smart_invest(capitals, profits, initial_capital, num_projects):
    max_heap = []
    min_heap = []

    for i in range(len(capitals)):
        heappush(min_heap, (capitals[i], i))

    available_capital = initial_capital
    for _ in range(num_projects):
        while min_heap and min_heap[0][0] <= available_capital:
            _, i = heappop(min_heap)
            heappush(max_heap, (-profits[i], i))

        if not max_heap:
            break

        available_capital += -heappop(max_heap)[0]

    return available_capital


@pytest.mark.parametrize(
    "capitals, profits, capital, nproj, expected",
    [
        ([0, 1, 2], [1, 2, 3], 1, 2, 6),
        ([0, 1, 2, 3], [1, 2, 3, 5], 0, 3, 8),
    ],
)
def test_grokking(capitals, profits, capital, nproj, expected):
    assert smart_invest(capitals, profits, capital, nproj) == expected
    assert smart_invest_custom(capitals, profits, capital, nproj) == expected


@pytest.mark.parametrize(
    "capitals, profits, capital, nproj, expected",
    [
        ([0, 1, 2], [1, 2, 3], 0, 10, 6),
        ([0, 9, 10], [1, 2, 3], 0, 2, 1),
    ],
)
def test_leetcode(capitals, profits, capital, nproj, expected):
    assert smart_invest(capitals, profits, capital, nproj) == expected
    assert smart_invest_custom(capitals, profits, capital, nproj) == expected
