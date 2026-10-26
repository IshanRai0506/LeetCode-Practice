
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        def dfs(r, c):
            visited[r][c] = True
            total = grid[r][c]

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and 0 <= nc < n
                    and grid[nr][nc] > 0
                    and not visited[nr][nc]):
                    total += dfs(nr, nc)

            return total

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and not visited[r][c]:
                    island_sum = dfs(r, c)

                    if island_sum % k == 0:
                        count += 1

        return count