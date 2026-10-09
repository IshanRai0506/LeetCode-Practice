class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        need = 0

        for ch in s:
            if ch == '(':
                need += 2

                if need % 2:
                    ans += 1
                    need -= 1

            else:  # ch == ')'
                need -= 1

                if need == -1:
                    ans += 1
                    need = 1

        return ans + need