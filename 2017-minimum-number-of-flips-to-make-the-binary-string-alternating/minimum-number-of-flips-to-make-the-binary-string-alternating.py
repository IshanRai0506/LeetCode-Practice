class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s2 = s + s
        
        # Build alternating patterns
        alt1 = "".join(str(i % 2) for i in range(2 * n))   # 0101...
        alt2 = "".join(str((i + 1) % 2) for i in range(2 * n))  # 1010...
        
        res = n
        diff1 = diff2 = 0
        
        # Sliding window
        for i in range(2 * n):
            if s2[i] != alt1[i]:
                diff1 += 1
            if s2[i] != alt2[i]:
                diff2 += 1
            
            if i >= n:
                if s2[i - n] != alt1[i - n]:
                    diff1 -= 1
                if s2[i - n] != alt2[i - n]:
                    diff2 -= 1
            
            if i >= n - 1:
                res = min(res, diff1, diff2)
        
        return res
