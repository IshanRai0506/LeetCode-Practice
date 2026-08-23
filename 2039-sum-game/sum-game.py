class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        sumL = sum(int(c) for c in num[:half] if c != '?')
        sumR = sum(int(c) for c in num[half:] if c != '?')
        qL = num[:half].count('?')
        qR = num[half:].count('?')

        # If total '?' is odd, Alice wins
        if (qL + qR) % 2 == 1:
            return True

        # Check if Bob can balance
        return (sumL - sumR) != (qR - qL) * 9 // 2
