class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        output = [0 for _ in range(n)]
        stack = []

        i = 0
        while i < n:
            if stack and temperatures[i] > temperatures[stack[-1]]:
                curr_idx = stack.pop()
                output[curr_idx] = i - curr_idx
            else:
                stack.append(i)
                i += 1

        return output


def test():
    assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ]
