"""
Problem Challenge 2

Maximum CPU Load (hard)

We are given a list of Jobs. Each job has a Start time, an End time, and a CPU
load when it is running. Our goal is to find the maximum CPU load at any time
if all the jobs are running on the same machine.

Example 1
Jobs: [[1,4,3], [2,5,4], [7,9,6]]
Output: 7
Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7)
will be when both the jobs are running at the same time i.e., during the time
interval (2,4).

Example 2
Jobs: [[6,7,10], [2,4,11], [8,12,15]]
Output: 15
Explanation: None of the jobs overlap, therefore we will take the maximum load
of any job which is 15.

Example 3
Jobs: [[1,4,2], [2,4,1], [3,6,5]]
Output: 8
Explanation: Maximum CPU load will be 8 as all jobs overlap during the time
interval [3,4].
"""


class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        # min heap based on job.end
        return self.end < other.end


def find_max_cpu_load(jobs: list[Job]) -> int:
    jobs.sort(key=lambda x: x.start)

    res = jobs[0].cpu_load

    for idx in range(1, len(jobs)):
        if min(jobs[idx].end, jobs[idx - 1].end) >= jobs[idx].start:
            res += jobs[idx].cpu_load
            continue

        res = max(res, jobs[idx].cpu_load)

    return res


def test_grokking():
    fn = find_max_cpu_load

    assert fn([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)]) == 7
    assert fn([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)]) == 15
    assert fn([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)]) == 8
