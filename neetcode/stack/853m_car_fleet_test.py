class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = zip(position, speed)
        stack = []
        for pos, spd in sorted(pairs, reverse=True):
            stack.append((target - pos) / spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

