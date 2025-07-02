# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         result = {}
#         for num in nums:
#             if num in result:
#                 del result[num]
#             else:
#                 result[num] = 1
#         return next(iter(result))

# XOR 비트 연산을 사용하면 아주 쉽게 해결할 수 있음. 
# XOR 자기 자신을 하면 0이 됨. 0과 자신을 XOR 연산하면 자기 자신이 됨. 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR 연산
        return result
