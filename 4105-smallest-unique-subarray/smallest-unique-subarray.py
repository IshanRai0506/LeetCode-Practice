
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        values = {v: i + 1 for i, v in enumerate(sorted(set(nums)))}
        s = [values[x] for x in nums] + [0]

        N = n + 1
        p = sorted(range(N), key=lambda i: s[i])

        c = [0] * N
        for i in range(1, N):
            c[p[i]] = c[p[i - 1]] + (s[p[i]] != s[p[i - 1]])

        length = 1

        while length < N:
            pn = [(x - length) % N for x in p]

            classes = max(c) + 1
            cnt = [0] * classes

            for x in pn:
                cnt[c[x]] += 1

            pos = [0] * classes
            for i in range(1, classes):
                pos[i] = pos[i - 1] + cnt[i - 1]

            p_new = [0] * N

            for x in pn:
                cl = c[x]
                p_new[pos[cl]] = x
                pos[cl] += 1

            p = p_new
            c_new = [0] * N

            for i in range(1, N):
                cur, prev = p[i], p[i - 1]

                a = (c[cur], c[(cur + length) % N])
                b = (c[prev], c[(prev + length) % N])

                c_new[cur] = c_new[prev] + (a != b)

            c = c_new
            length *= 2

        sa = p[1:]

        rank = [0] * n
        for i, x in enumerate(sa):
            rank[x] = i

        lcp = [0] * n
        k = 0

        for i in range(n):
            r = rank[i]

            if r == 0:
                k = 0
                continue

            j = sa[r - 1]

            while i + k < n and j + k < n:
                if nums[i + k] != nums[j + k]:
                    break
                k += 1

            lcp[r] = k

            if k:
                k -= 1

        ans = n

        for i in range(n):
            r = rank[i]

            common = lcp[r]

            if r + 1 < n:
                common = max(common, lcp[r + 1])

            candidate = common + 1

            if candidate <= n - i:
                ans = min(ans, candidate)

        return ans