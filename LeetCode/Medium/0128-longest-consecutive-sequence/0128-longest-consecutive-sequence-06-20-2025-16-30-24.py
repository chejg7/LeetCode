class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # dic = {}
        # for num in nums:
        #     if num - 1 in dic:
        #         dic[num] = dic[num - 1] + 1
        #     else:
        #         dic[num] = 1
        # return max(dic.values())

        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = 1
                while num + 1 in num_set:
                    current += 1
                    num += 1
                max_length = max(max_length, current)
        return max_length