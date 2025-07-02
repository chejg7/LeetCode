class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = {}
        for num in nums:
            if num in result:
                del result[num]
            else:
                result[num] = 1
        return next(iter(result))