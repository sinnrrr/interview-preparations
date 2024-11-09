class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def can_attend_meetings(self, intervals: list[Interval]) -> bool:
        busy_at = [0, 0]
        for interval in intervals:
            if interval.start < busy_at[1]:
                return False
            busy_at = [
                min(interval.start, busy_at[0]),
                max(interval.end, busy_at[0]),
            ]
        return True
