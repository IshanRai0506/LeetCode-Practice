
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        min_price = min(price for factor, price in items)
        max_factor = max(factor for factor, price in items)

        freq = [0] * (max_factor + 1)

        for factor, price in items:
            freq[factor] += 1

        # Count all item types whose factors are multiples
        for i in range(1, max_factor + 1):
            for j in range(i * 2, max_factor + 1, i):
                freq[i] += freq[j]

        # Collect items that can generate free copies
        candidates = []

        for factor, price in items:
            free_count = freq[factor] - 1

            if free_count > 0 and price <= 2 * min_price:
                candidates.append((price, free_count))

        # Buy the cheapest boosted copies first
        candidates.sort()

        ans = 0

        for price, count in candidates:
            take = min(count, budget // price)

            ans += take * 2
            budget -= take * price

        # Spend remaining budget on the cheapest item
        ans += budget // min_price

        return ans
