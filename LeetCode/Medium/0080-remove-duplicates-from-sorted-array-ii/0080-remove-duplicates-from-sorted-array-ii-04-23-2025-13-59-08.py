class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        k = [nums[0], 1]
        while i < len(nums):
            if nums[i] == k[0]:
                k[1] += 1
                if k[1] > 2:
                    del nums[i]
                else:
                    i += 1
            else:
                k = [nums[i], 1]
                i += 1
        return i
            