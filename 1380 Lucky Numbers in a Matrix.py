class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        mins = set([min(row) for row in matrix])
        maxes = set([max([matrix[i][j] for i in range(m)]) for j in range(n)])

        return list(mins & maxes)
