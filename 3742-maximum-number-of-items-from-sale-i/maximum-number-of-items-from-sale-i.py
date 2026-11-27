
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n = len(items)

        # Step 1: Calculate free items for each item
        weight = []

        for i in range(n):
            free = 0

            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free += 1

            weight.append(free + 1)

        # Step 2: Group items according to their prices
        groups = {}

        for i in range(n):
            factor, price = items[i]

            if price <= budget:
                groups.setdefault(price, []).append(weight[i])

        # Step 3: DP for items with higher prices
        dp = [-1] * (budget + 1)
        dp[0] = 0

        ans = 0

        # Process prices from high to low
        for p in sorted(groups.keys(), reverse=True):

            # At least one item with price p must be selected
            curr = [-1] * (budget + 1)

            for w in groups[p]:

                for c in range(budget, p - 1, -1):

                    if dp[c - p] != -1:
                        curr[c] = max(
                            curr[c],
                            dp[c - p] + w
                        )

                    if curr[c - p] != -1:
                        curr[c] = max(
                            curr[c],
                            curr[c - p] + w
                        )

            # Step 4: Calculate maximum total items
            for c in range(budget + 1):
                if curr[c] != -1:
                    extra = (budget - c) // p
                    ans = max(ans, curr[c] + extra)

            # Step 5: Add current-price items to regular DP
            for w in groups[p]:
                for c in range(budget, p - 1, -1):
                    if dp[c - p] != -1:
                        dp[c] = max(
                            dp[c],
                            dp[c - p] + w
                        )

        return ans