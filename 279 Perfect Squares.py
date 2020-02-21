class Solution:
    def numSquares(self, n: int) -> int:
        import math

        if math.sqrt(n).is_integer():
            return 1
        else:
            while not (n % 4):
                n >>= 2

            if n % 8 == 7:
                return 4
            else:
                for i in range(1, int(math.sqrt(n)) + 1):
                    if math.sqrt(n - i ** 2).is_integer():
                        return 2
                return 3

        return A[n]
