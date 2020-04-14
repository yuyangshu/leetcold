class Solution:
    def numSteps(self, s: str) -> int:
        target = 0

        for i in range(0, len(s)):
            target *= 2
            target += ord(s[i]) - ord('0')

        counter = 0
        while target != 1:
            counter += 1
            if target % 2 == 1:
                target += 1
            else:
                target //= 2

        return counter
