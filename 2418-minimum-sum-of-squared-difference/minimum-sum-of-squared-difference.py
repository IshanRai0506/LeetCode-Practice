from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        total = sum(diff)
        if total <= k:
            return 0

        # Binary search final maximum difference
        lo, hi = 0, max(diff)

        while lo < hi:
            mid = (lo + hi) // 2

            need = 0
            for d in diff:
                if d > mid:
                    need += d - mid

            if need <= k:
                hi = mid
            else:
                lo = mid + 1

        x = lo

        arr = []
        used = 0

        for d in diff:
            if d > x:
                used += d - x
                arr.append(x)
            else:
                arr.append(d)

        rem = k - used

        # Reduce some x's to x-1 using remaining operations
        for i in range(len(arr)):
            if rem == 0:
                break
            if arr[i] == x:
                arr[i] -= 1
                rem -= 1

        ans = 0
        for d in arr:
            ans += d * d

        return ans