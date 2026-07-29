class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case
        if n == 1:
            return "0"
        
        mid = 1 << (n - 1)  # 2^(n-1)
        
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            # mirrored position in the left half
            mirrored = mid - (k - mid)
            bit = self.findKthBit(n - 1, mirrored)
            return "1" if bit == "0" else "0"

