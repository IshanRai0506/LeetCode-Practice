class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        n = len(s)

        for i in range(n - 1, -1, -1):
            remaining = count[:]

            # Match target prefix
            possible = True

            for j in range(i):
                idx = ord(target[j]) - ord('a')

                if remaining[idx] == 0:
                    possible = False
                    break

                remaining[idx] -= 1

            if not possible:
                continue

            # Find smallest character greater than target[i]
            target_idx = ord(target[i]) - ord('a')

            for c in range(target_idx + 1, 26):
                if remaining[c] > 0:
                    remaining[c] -= 1

                    ans = target[:i] + chr(c + ord('a'))

                    # Add remaining characters in sorted order
                    for k in range(26):
                        ans += chr(k + ord('a')) * remaining[k]

                    return ans

        return ""