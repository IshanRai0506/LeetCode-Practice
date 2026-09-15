class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[l][r] = True if s[l:r+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        for i in range(n):
            pal[i][i] = True

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] == s[r] and (length <= 2 or pal[l + 1][r - 1]):
                    pal[l][r] = True

        # dp[i] = maximum number of valid palindromes
        # using s[0:i]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Don't take a palindrome ending at i-1
            dp[i] = dp[i - 1]

            # Try every palindrome ending at i-1
            for l in range(i - k + 1):
                if i - l >= k and pal[l][i - 1]:
                    dp[i] = max(dp[i], dp[l] + 1)

        return dp[n]