class Solution:

    def __init__(self, w: List[int]):
        import random

        self.upper = [0] * len(w)
        for i in range(len(w)):
            self.upper[i] = w[i] + (self.upper[i - 1] if i > 0 else 0)

    def pickIndex(self) -> int:
        target = random.randrange(1, self.upper[-1] + 1)

        i, j = 0, len(self.upper) - 1

        while i < j:
            mid = (i + j) // 2
            if self.upper[mid] < target:
                i = mid + 1
            else:
                j = mid

        return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
