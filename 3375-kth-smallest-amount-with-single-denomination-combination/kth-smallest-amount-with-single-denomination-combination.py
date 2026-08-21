from math import gcd
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Remove redundant coins (divisible by smaller ones)
        coins.sort()
        filtered = []
        for c in coins:
            if all(c % f != 0 for f in filtered):
                filtered.append(c)
        
        def count(x):
            total = 0
            n = len(filtered)
            # Inclusion-exclusion principle
            for r in range(1, n+1):
                for comb in combinations(filtered, r):
                    lcm = comb[0]
                    for c in comb[1:]:
                        lcm = lcm * c // gcd(lcm, c)
                    total += (-1)**(r+1) * (x // lcm)
            return total
        
        # Binary search
        left, right = 1, 10**18
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left
