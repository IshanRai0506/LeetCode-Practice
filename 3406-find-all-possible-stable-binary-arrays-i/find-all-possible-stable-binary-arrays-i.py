class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        # dp[z][o][last] = ways
        dp = [[[0, 0] for _ in range(one+1)] for _ in range(zero+1)]

        # Initialize: start with a run of zeros or ones
        for run in range(1, min(limit, zero) + 1):
            dp[run][0][0] = 1
        for run in range(1, min(limit, one) + 1):
            dp[0][run][1] = 1

        for z in range(zero+1):
            for o in range(one+1):
                for last in (0, 1):
                    cur = dp[z][o][last]
                    if cur == 0:
                        continue
                    if last == 0:
                        # add ones
                        for run in range(1, min(limit, one - o) + 1):
                            dp[z][o+run][1] = (dp[z][o+run][1] + cur) % MOD
                    else:
                        # add zeros
                        for run in range(1, min(limit, zero - z) + 1):
                            dp[z+run][o][0] = (dp[z+run][o][0] + cur) % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
