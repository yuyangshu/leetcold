class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        A = [[0] * n for _ in range(m) ]

        for i in range(m):
            if not obstacleGrid[i][0]:
                A[i][0] = 1
            else:
                break

        for i in range(n):
            if not obstacleGrid[0][i]:
                A[0][i] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    A[i][j] = A[i - 1][j] + A[i][j - 1]

        return A[m - 1][n - 1]
