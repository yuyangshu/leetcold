class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            result = int('-' + str(-x)[::-1])
        else:
            result = int(str(x)[::-1])

        return 0 if result < -pow(2, 31) or result > pow(2, 31) - 1 else result
