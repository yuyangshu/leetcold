class Solution:
    def numOfWays(self, n: int) -> int:
        double = [6] + [0] * (n - 1)
        triple = [6] + [0] * (n - 1)

        for i in range(1, n):
            double[i] = (double[i - 1] * 3 + triple[i - 1] * 2) % (10 ** 9 + 7)
            triple[i] = (double[i - 1] * 2 + triple[i - 1] * 2) % (10 ** 9 + 7)

        return (double[-1] + triple[-1]) % (10 ** 9 + 7)
