class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # If "01" appears in the string, then there is more than one segment of ones
        return "01" not in s
