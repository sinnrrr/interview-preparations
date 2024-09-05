class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            mid_row, mid_col = divmod(mid, n)

            if target == matrix[mid_row][mid_col]:
                return True
            elif target > matrix[mid_row][mid_col]:
                left = mid + 1
            elif target < matrix[mid_row][mid_col]:
                right = mid - 1

        return False
