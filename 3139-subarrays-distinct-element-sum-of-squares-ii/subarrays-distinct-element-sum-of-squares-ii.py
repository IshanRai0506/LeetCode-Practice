from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n
        tree = [[0, 0, 0] for _ in range(size)]

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                length = r - l + 1
                s, sq, lazy = tree[node]
                tree[node][1] = (sq + 2 * s + length) % MOD
                tree[node][0] = (s + length) % MOD
                tree[node][2] = lazy + 1
                return

            mid = (l + r) // 2
            push(node, l, r)

            if ql <= mid:
                update(node * 2, l, mid, ql, qr)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr)

            tree[node][0] = (tree[node * 2][0] + tree[node * 2 + 1][0]) % MOD
            tree[node][1] = (tree[node * 2][1] + tree[node * 2 + 1][1]) % MOD

        def push(node, l, r):
            lazy = tree[node][2]
            if lazy == 0 or l == r:
                return

            mid = (l + r) // 2
            for child, a, b in (
                (node * 2, l, mid),
                (node * 2 + 1, mid + 1, r)
            ):
                length = b - a + 1
                s, sq, old = tree[child]
                tree[child][1] = (sq + 2 * lazy * s + lazy * lazy * length) % MOD
                tree[child][0] = (s + lazy * length) % MOD
                tree[child][2] += lazy

            tree[node][2] = 0

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1
            update(1, 0, n - 1, left, i)
            ans = (ans + tree[1][1]) % MOD
            last[x] = i

        return ans