class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[c] = [ways arriving from left (dir 0), ways arriving from top (dir 1)]
        dp = [[0, 0] for _ in range(n + 1)]
        
        # Base case: at (0, 0), 1 path available for moving right, 1 for moving down
        dp[1] = [1, 1]
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # Mirror cell: swaps directions across coordinates
                    dp[c + 1] = [dp[c + 1][1], dp[c][0]]
                else:
                    # Empty cell: sums incoming paths from left and top
                    total = (dp[c + 1][1] + dp[c][0]) % MOD
                    dp[c + 1] = [total, total]
                    
        return dp[n][0]