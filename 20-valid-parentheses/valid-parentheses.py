class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in mp:
                if not stack or stack.pop() != mp[ch]:
                    return False
            else:
                stack.append(ch)

        return not stack