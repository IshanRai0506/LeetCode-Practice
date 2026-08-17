class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        # Alice must start with remainder 1 or 2.
        if cnt[1] == 0 and cnt[2] == 0:
            return False

        # Remove all possible remainder-0 stones conceptually.
        # Their effect depends on whether their count is even or odd.
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0

        return abs(cnt[1] - cnt[2]) > 2