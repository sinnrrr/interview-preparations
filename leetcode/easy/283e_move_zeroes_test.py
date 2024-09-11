class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n, i, j = len(nums), 0, 0
        while i < n and j < n:
            while j < n - 1 and nums[j] == 0:
                j += 1
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1

        """
        0: [0,1,0,3,12], i=0, j=0
        1: [1,0,0,3,12], i=0, j=1
        2: [1,0,0,3,12], i=1, j=2
        3: [1,3,0,0,12], i=1, j=3
        4: [1,3,12,0,0], i=2, j=4
        """


def test():
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]
