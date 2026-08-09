from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Precompute suffix sums for quick access
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        @lru_cache(None)
        def dp(i: int, M: int) -> int:
            # If no piles left
            if i >= n:
                return 0
            # If Alice can take all remaining piles
            if i + 2 * M >= n:
                return suffix_sum[i]
            
            best = 0
            # Try all possible X (number of piles to take)
            for X in range(1, 2 * M + 1):
                # Alice takes suffix_sum[i] - (what Bob can force her to leave)
                best = max(best, suffix_sum[i] - dp(i + X, max(M, X)))
            return best
        
        return dp(0, 1)
