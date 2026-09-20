class Solution:
    def reverseDegree(self, s: str) -> int:
        total =0
        for i ,ch in enumerate(s):
            reverse_position = ord('z') - ord(ch) + 1
            string_position = i + 1

            total += reverse_position * string_position

        return total