class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        from bisect import bisect_right

        n = len(intervals)

        # l, r, weight, original index
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort by starting position
        arr.sort()

        starts = [x[0] for x in arr]

        # Find first interval with start > current end
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        # dp[i][k] = (maximum score, lexicographically smallest indices)
        # using intervals from i onward and at most k intervals
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        def better(a, b):
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            return a if a[1] < b[1] else b

        for i in range(n - 1, -1, -1):
            l, r, w, idx = arr[i]

            for k in range(1, 5):

                # Don't take current interval
                skip = dp[i + 1][k]

                # Take current interval
                j = nxt[i]
                future = dp[j][k - 1]

                take = (
                    w + future[0],
                    tuple(sorted((idx,) + future[1]))
                )

                dp[i][k] = better(skip, take)

        return list(dp[0][4][1])