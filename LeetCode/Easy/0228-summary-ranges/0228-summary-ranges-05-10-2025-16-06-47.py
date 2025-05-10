class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        while i < len(nums):
            start = i
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            ran = str(nums[start]) + "->" + str(nums[i]) if i > start else str(nums[start])
            result.append(ran)
            i += 1
        return result
