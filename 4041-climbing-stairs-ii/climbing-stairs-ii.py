class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] + [float('inf')] * n

        for i in range(1, n + 1):
            dp[i] = costs[i - 1] + min(
                dp[j] + (i - j) ** 2
                for j in range(max(0, i - 3), i)
            )

        return dp[n]