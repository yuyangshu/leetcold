class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        A = [[0] * n for _ in range(m) ]

        for i in range(m):
            A[i][0] = 1

        for i in range(n):
            A[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                A[i][j] = A[i - 1][j] + A[i][j - 1]

        return A[m - 1][n - 1]
