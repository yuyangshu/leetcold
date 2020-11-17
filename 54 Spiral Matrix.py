class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        bounds = [0, n - 1, m - 1, 0]       # bounds change in this order

        def in_bound(i, j, bounds):
            return bounds[0] <= i <= bounds[2] and bounds[3] <= j <= bounds[1]

        i, j, turns, results = 0, -1, 0, []
        for _ in range(m * n):
            print(i, j, turns, bounds)
            if not in_bound(i + directions[turns % 4][0], j + directions[turns % 4][1], bounds):
                bounds[turns % 4] += 1 if turns % 4 in {0, 3} else -1
                turns += 1
            i += directions[turns % 4][0]
            j += directions[turns % 4][1]
            results.append(matrix[i][j])

        return results
