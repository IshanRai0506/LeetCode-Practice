class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        pushes = 0
        for i in range(n):
            # Each block of 8 letters increases the push count
            pushes += (i // 8) + 1
        return pushes
