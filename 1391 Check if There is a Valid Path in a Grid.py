class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        target_mapping = {
            1: [(0, -1, {1, 4, 6}), (0, 1, {1, 3, 5})],
            2: [(-1, 0, {2, 3, 4}), (1, 0, {2, 5, 6})],
            3: [(0, -1, {1, 4, 6}), (1, 0, {2, 5, 6})],
            4: [(0, 1, {1, 3, 5}), (1, 0, {2, 5, 6})],
            5: [(-1, 0, {2, 3, 4}), (0, -1, {1, 4, 6})],
            6: [(-1, 0, {2, 3, 4}), (0, 1, {1, 3, 5})]
        }

        def find(A):
            return A if uf[A] == A else find(uf[A])

        def union(A, B):
            uf[find(A)] = uf[find(B)]

        m, n = len(grid), len(grid[0])
        uf = {
            (i, j): (i, j) for i in range(m) for j in range(n)
        }

        for i in range(m):
            for j in range(n):
                for spec in target_mapping[grid[i][j]]:
                    target = (i + spec[0], j + spec[1])
                    if 0 <= target[0] < m and 0 <= target[1] < n and grid[target[0]][target[1]] in spec[2]:
                        uf[find(target)] = uf[find((i, j))]

        return find((0, 0)) == find((m - 1, n - 1))
