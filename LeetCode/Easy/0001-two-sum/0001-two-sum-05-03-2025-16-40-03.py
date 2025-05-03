class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 아래의 코드는 시간 복잡도가 O(n)

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         num_map = {}  # 숫자 → 인덱스
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_map:
#                 return [num_map[complement], i]
#             num_map[num] = i
