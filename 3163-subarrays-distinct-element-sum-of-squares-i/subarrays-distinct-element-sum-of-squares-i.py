class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            distinct = set()

            for j in range(i,n):
                distinct.add(nums[j])

                cnt = len(distinct)  
                ans += cnt * cnt

        return ans      