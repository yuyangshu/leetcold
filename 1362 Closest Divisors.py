class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        from math import sqrt, floor

        apart = float("inf")

        for target in [num + 1, num + 2]:
            for i in range(floor(sqrt(target)), 0, -1):
                if target % i == 0 and abs(target // i - i) < apart:
                    a, b = i, target // i
                    apart = abs(target // i - i)

        return [a, b]
