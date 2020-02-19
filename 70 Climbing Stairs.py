class Solution:
    def climbStairs(self, n: int) -> int:
        n += 1
        A = [1] * n

        for i in range(2, n):
            A[i] = A[i - 2] + A[i - 1]

        return A[-1]
