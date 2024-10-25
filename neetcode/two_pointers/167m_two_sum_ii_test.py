class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lp, rp = 0, len(numbers) - 1

        while lp <= rp:
            curr = numbers[rp] + numbers[lp]
            if curr == target:
                return [lp + 1, rp + 1]
            if curr < target:
                lp += 1
            if curr > target:
                rp -= 1

        return [-1, -1]
