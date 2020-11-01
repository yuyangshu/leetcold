class Solution:
    def countVowelStrings(self, n: int) -> int:
        row = [1, 1, 1, 1, 1]

        for i in range(1, n):
            row = [
                row[0] + row[1] + row[2] + row[3] + row[4],
                row[1] + row[2] + row[3] + row[4],
                row[2] + row[3] + row[4],
                row[3] + row[4],
                row[4],
            ]

        return sum(row)
