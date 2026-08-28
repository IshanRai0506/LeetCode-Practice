class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:

        n = len(s)

        # Count characters
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Check whether palindrome is possible
        odd = 0
        mid = ""

        for i in range(26):
            if freq[i] % 2:
                odd += 1
                mid = chr(ord('a') + i)

        if odd > 1:
            return ""

        # We only need to arrange half of the characters.
        half_count = [x // 2 for x in freq]
        half_len = n // 2

        # Build palindrome
        def make_pal(left):
            left = ''.join(left)

            if n % 2 == 0:
                return left + left[::-1]

            return left + mid + left[::-1]

        # -------------------------------------------------
        # Find the smallest possible LEFT HALF
        # whose palindrome is > target.
        #
        # We build from left to right.
        # At every position:
        #
        #   1. Try equal to target
        #   2. Try a character greater than target
        #
        # Once greater, fill everything else minimally.
        # -------------------------------------------------

        answer = None

        def dfs(pos, count, left, relation):

            nonlocal answer

            # relation:
            # -1 = palindrome prefix is smaller
            #  0 = equal so far
            #  1 = greater already

            if pos == half_len:

                candidate = make_pal(left)

                if candidate > target:
                    if answer is None or candidate < answer:
                        answer = candidate

                return

            # If we already have a better answer,
            # don't explore prefixes that cannot improve it.
            if answer is not None:
                current_prefix = ''.join(left)

                if len(current_prefix) > 0:
                    if current_prefix > answer[:pos]:
                        return

            # Try characters in lexicographical order
            for c in range(26):

                if count[c] == 0:
                    continue

                ch = chr(ord('a') + c)

                # Determine how this character compares
                # with target at this position.
                if relation == 0:

                    if ch < target[pos]:
                        # This makes the palindrome smaller
                        # at its first differing position.
                        continue

                    new_relation = 0 if ch == target[pos] else 1

                else:
                    # Already greater, so any character is allowed
                    new_relation = 1

                count[c] -= 1
                left.append(ch)

                dfs(pos + 1, count, left, new_relation)

                left.pop()
                count[c] += 1

        dfs(0, half_count[:], [], 0)

        return answer if answer is not None else ""