from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count frequency of each letter
        freq = Counter(word)
        
        # Sort frequencies in descending order
        counts = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        for i, count in enumerate(counts):
            # Determine push cost based on position
            # Every 8 letters, the push cost increases by 1
            push_cost = (i // 8) + 1
            total_pushes += count * push_cost
        
        return total_pushes
