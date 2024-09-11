class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1, p2, write_idx = m - 1, n - 1, m + n - 1

        while p2 >= 0:
            if p1 >= 0 and nums2[p2] >= nums1[p1]:
                nums1[write_idx] = nums2[p2]
                nums2[p2] = 0
                p2 -= 1
            elif nums2[p2] < nums1[p1]:
                nums1[write_idx] = nums1[p1]
                nums1[p1] = 0
                p1 -= 1
            write_idx -= 1
