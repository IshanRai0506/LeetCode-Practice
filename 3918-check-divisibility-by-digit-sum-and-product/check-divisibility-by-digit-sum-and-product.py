class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # Calculate digit sum
        digit_sum = sum(int(d) for d in str(n))
        
        # Calculate digit product
        digit_product = 1
        for d in str(n):
            digit_product *= int(d)
        
        # Total = digit sum + digit product
        total = digit_sum + digit_product
        
        # Check divisibility
        return n % total == 0
