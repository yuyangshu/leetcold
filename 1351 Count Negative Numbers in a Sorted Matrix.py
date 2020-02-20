class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        count = 0

        for row in grid:
            i, j = 0, n - 1
            while i < j:
                mid = (i + j) // 2
                if row[mid] >= 0:
                    i = mid + 1
                else:
                    j = mid

            if row[i] < 0:
                count += n - i

        return count
