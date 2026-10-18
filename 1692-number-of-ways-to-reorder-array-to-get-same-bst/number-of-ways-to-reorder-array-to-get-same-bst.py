
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute combinations using Pascal's triangle
        comb = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            comb[i][0] = comb[i][i] = 1
            for j in range(1, i):
                comb[i][j] = (comb[i - 1][j - 1] +
                              comb[i - 1][j]) % MOD

        def solve(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            left_ways = solve(left)
            right_ways = solve(right)

            ways = comb[len(arr) - 1][len(left)]
            ways = ways * left_ways % MOD
            ways = ways * right_ways % MOD

            return ways

        return (solve(nums) - 1) % MOD
