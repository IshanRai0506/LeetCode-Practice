from typing import List

class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: Compute prefix max
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])
        
        # Step 2: Compute suffix min
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], nums[i])
        
        # Step 3: Find smallest stable index
        for i in range(n):
            instability = prefix_max[i] - suffix_min[i]
            if instability <= k:
                return i
        
        return -1
