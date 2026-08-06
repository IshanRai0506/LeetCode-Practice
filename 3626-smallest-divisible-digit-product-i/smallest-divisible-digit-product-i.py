class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(x: int) -> int:
            prod = 1
            for d in str(x):
                prod *= int(d)
            return prod
        
        while True:
            if digit_product(n) % t == 0:
                return n
            n += 1
