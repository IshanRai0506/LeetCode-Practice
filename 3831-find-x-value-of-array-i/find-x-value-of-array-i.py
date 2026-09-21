class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            x = num % k
            ndp = [0] * k

            ndp[x] += 1

            for r in range(k):
                if dp[r]:
                    ndp[(r * x) % k] += dp[r]

            dp = ndp

            for r in range(k):
                ans[r] += dp[r]

        return ans