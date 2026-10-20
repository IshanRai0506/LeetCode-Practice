
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        pref_max = [0] * (n + 1)
        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        suff_min = [float('inf')] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        drops = [0] * n
        for i in range(1, n):
            drops[i] = drops[i - 1] + (nums[i - 1] > nums[i])

        def check(k):
            for start in range(0, n, k):
                end = start + k - 1

                count = drops[end] - drops[start]
                if nums[end] > nums[start]:
                    count += 1

                if count > 1 or pref_max[start] > suff_min[start]:
                    return False

            return True

        ans = 0
        d = 1

        while d * d <= n:
            if n % d == 0:
                if check(d):
                    ans += d

                other = n // d
                if other != d and check(other):
                    ans += other

            d += 1

        return ans