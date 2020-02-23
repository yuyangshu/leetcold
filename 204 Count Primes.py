class Solution:
    def countPrimes(self, n: int) -> int:
        from math import sqrt, ceil

        primes = [1] * n

        for i in range(2, ceil(sqrt(n))):
            for j in range(i ** 2, n, i):
                primes[j] = 0

        return sum(primes[2:])
