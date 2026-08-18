from collections import defaultdict
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Dictionary to track in how many subarrays each number appears
        count_in_subarrays = defaultdict(int)
        
        # Sliding window to cover all subarrays of size k
        for i in range(n - k + 1):
            window = nums[i:i+k]
            unique_in_window = set(window)
            for num in unique_in_window:
                count_in_subarrays[num] += 1
        
        # Find the largest integer that appears in exactly one subarray
        result = -1
        for num, cnt in count_in_subarrays.items():
            if cnt == 1:
                result = max(result, num)
        
        return result
