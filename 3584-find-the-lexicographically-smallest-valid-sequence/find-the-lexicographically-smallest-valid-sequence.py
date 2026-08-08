class Solution:
    def validSequence(self, word1: str, word2: str):
        n, m = len(word1), len(word2)
        
        # Step 1: Build dp array
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]
            if dp[i + 1] < m and word1[i] == word2[m - dp[i + 1] - 1]:
                dp[i] = dp[i + 1] + 1

        # Step 2: Greedy selection
        res, j, mismatch_used = [], 0, False
        for i in range(n):
            if j < m:
                if word1[i] == word2[j]:
                    res.append(i)
                    j += 1
                elif not mismatch_used and dp[i + 1] >= m - j - 1:
                    # Use mismatch here
                    res.append(i)
                    j += 1
                    mismatch_used = True

        return res if j == m else []
