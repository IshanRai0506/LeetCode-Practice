class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # tree[node] = [product % k, prefix counts]
        tree = [[1, [0] * k] for _ in range(4 * n)]

        def merge(a, b):
            total_a, count_a = a
            total_b, count_b = b

            total = (total_a * total_b) % k
            count = count_a[:]

            for r in range(k):
                new_r = (total_a * r) % k
                count[new_r] += count_b[r]

            return [total, count]

        def build(node, l, r):
            if l == r:
                rem = nums[l] % k
                tree[node] = [rem, [0] * k]
                tree[node][1][rem] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, value):
            if l == r:
                rem = value % k
                tree[node] = [rem, [0] * k]
                tree[node][1][rem] = 1
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            # Update persists for future queries
            update(1, 0, n - 1, index, value)

            # Count valid remaining prefixes of nums[start:]
            result = query(1, 0, n - 1, start, n - 1)

            ans.append(result[1][x])

        return ans