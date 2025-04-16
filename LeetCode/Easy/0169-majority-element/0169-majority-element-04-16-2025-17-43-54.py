class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        memo = {}
        for n in nums:
            if n in memo:
                memo[n] += 1
            else:
                memo[n] = 0
        return max(memo, key=memo.get)
        