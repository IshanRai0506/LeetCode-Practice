class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        has_odd = any(x % 2 for x in nums1)

        # Already all even
        if not has_odd:
            return True

        # If there is an odd number, use the smallest odd
        min_odd = min(x for x in nums1 if x % 2)

        # Every even number must be larger than the smallest odd
        return all(x % 2 == 1 or x > min_odd for x in nums1)