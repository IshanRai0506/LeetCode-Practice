class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        chars = list(s)
        v = [c for c in chars if c in vowels]
        for i in range(len(chars)):
            if chars[i] in vowels:
                chars[i] = v.pop()
        return "".join(chars)