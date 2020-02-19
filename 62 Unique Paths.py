class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        A = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                A[i][j] = A[i - 1][j] + A[i][j - 1]

        return A[m - 1][n - 1]
