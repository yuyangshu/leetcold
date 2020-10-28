class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        if not grid or not grid[0]:
            return 0
        else:
            m, n, count = len(grid), len(grid[0]), 0
            visited = [[False] * n for _ in range(m)]
            
            def is_valid(x, y):
                return 0 <= x < m and 0 <= y < n
            
            def mark_connections(x, y):
                visited[x][y] = True
                print(x, y, count)

                for delta_x, delta_y in directions:
                    target_x, target_y = x + delta_x, y + delta_y
                    if is_valid(target_x, target_y) and grid[target_x][target_y] == '1' and not visited[target_x][target_y]:
                        mark_connections(target_x, target_y)

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == '1' and not visited[i][j]:
                        mark_connections(i, j)
                        count += 1

            return count
