class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # 1. Factorize t into prime factors 2, 3, 5, 7
        temp = t
        factors = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in (2, 3, 5, 7):
            while temp % p == 0:
                factors[p] += 1
                temp //= p
        
        # If t has prime factors greater than 7, no digit product can be divisible by t
        if temp > 1:
            return "-1"
            
        req_a, req_b, req_c, req_d = factors[2], factors[3], factors[5], factors[7]

        # 2. Precompute DP table for minimum digits needed for a (2s) and b (3s)
        MAX_A, MAX_B = 60, 60
        dp = [[float('inf')] * (MAX_B + 1) for _ in range(MAX_A + 1)]
        dp[0][0] = 0
        transitions = [(1, 0), (0, 1), (2, 0), (1, 1), (3, 0), (0, 2)]

        for a in range(MAX_A + 1):
            for b in range(MAX_B + 1):
                if dp[a][b] == float('inf'):
                    continue
                for da, db in transitions:
                    na = min(MAX_A, a + da)
                    nb = min(MAX_B, b + db)
                    dp[na][nb] = min(dp[na][nb], dp[a][b] + 1)

        for a in range(MAX_A, -1, -1):
            for b in range(MAX_B, -1, -1):
                if a < MAX_A:
                    dp[a][b] = min(dp[a][b], dp[a + 1][b])
                if b < MAX_B:
                    dp[a][b] = min(dp[a][b], dp[a][b + 1])

        def min_len(a, b, c, d):
            a, b, c, d = max(0, a), max(0, b), max(0, c), max(0, d)
            return dp[min(MAX_A, a)][min(MAX_B, b)] + c + d

        dig_facts = {
            1: (0, 0, 0, 0), 2: (1, 0, 0, 0), 3: (0, 1, 0, 0),
            4: (2, 0, 0, 0), 5: (0, 0, 1, 0), 6: (1, 1, 0, 0),
            7: (0, 0, 0, 1), 8: (3, 0, 0, 0), 9: (0, 2, 0, 0)
        }

        def build_smallest_suffix(k, a, b, c, d):
            a, b, c, d = max(0, a), max(0, b), max(0, c), max(0, d)
            needed = min_len(a, b, c, d)
            if k < needed:
                return None
            
            res = ['1'] * (k - needed)
            curr_k, curr_a, curr_b, curr_c, curr_d = needed, a, b, c, d
            for _ in range(needed):
                for dig in range(1, 10):
                    da, db, dc, dd = dig_facts[dig]
                    rem_a, rem_b = curr_a - da, curr_b - db
                    rem_c, rem_d = curr_c - dc, curr_d - dd
                    if curr_k - 1 >= min_len(rem_a, rem_b, rem_c, rem_d):
                        res.append(str(dig))
                        curr_a, curr_b, curr_c, curr_d = rem_a, rem_b, rem_c, rem_d
                        curr_k -= 1
                        break
            return "".join(res)

        n = len(num)
        min_overall_len = min_len(req_a, req_b, req_c, req_d)

        if min_overall_len > n:
            return build_smallest_suffix(min_overall_len, req_a, req_b, req_c, req_d)

        first_zero_idx = num.find('0')
        
        if first_zero_idx == -1:
            cur_a = cur_b = cur_c = cur_d = 0
            for ch in num:
                da, db, dc, dd = dig_facts[int(ch)]
                cur_a += da; cur_b += db; cur_c += dc; cur_d += dd
            if cur_a >= req_a and cur_b >= req_b and cur_c >= req_c and cur_d >= req_d:
                return num

        max_prefix_len = n if first_zero_idx == -1 else first_zero_idx

        pref_a = [0] * (max_prefix_len + 1)
        pref_b = [0] * (max_prefix_len + 1)
        pref_c = [0] * (max_prefix_len + 1)
        pref_d = [0] * (max_prefix_len + 1)

        for i in range(max_prefix_len):
            da, db, dc, dd = dig_facts[int(num[i])]
            pref_a[i + 1] = pref_a[i] + da
            pref_b[i + 1] = pref_b[i] + db
            pref_c[i + 1] = pref_c[i] + dc
            pref_d[i + 1] = pref_d[i] + dd

        for i in range(max_prefix_len, -1, -1):
            if i == n:
                continue
            
            start_dig = int(num[i]) + 1
            rem_len = n - 1 - i
            
            for dig in range(start_dig, 10):
                da, db, dc, dd = dig_facts[dig]
                rem_a = req_a - (pref_a[i] + da)
                rem_b = req_b - (pref_b[i] + db)
                rem_c = req_c - (pref_c[i] + dc)
                rem_d = req_d - (pref_d[i] + dd)
                
                if rem_len >= min_len(rem_a, rem_b, rem_c, rem_d):
                    prefix = num[:i] + str(dig)
                    suffix = build_smallest_suffix(rem_len, rem_a, rem_b, rem_c, rem_d)
                    return prefix + suffix

        target_len = max(n + 1, min_overall_len)
        return build_smallest_suffix(target_len, req_a, req_b, req_c, req_d)