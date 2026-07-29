from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        result = []
        for i in range(n):
            # Flip the i-th bit of nums[i]
            result.append('1' if nums[i][i] == '0' else '0')
        return "".join(result)
