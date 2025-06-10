# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         result = [[1]]
#         for i in range(1, numRows):
#             temp = []
#             for j in range(i + 1):
#                 if j == 0 or j == i:
#                     temp.append(1)
#                 else:
#                     temp.append(result[i - 1][j - 1] + result[i - 1][j])
#             result.append(temp)

#         return result

# 아래가 좀 더 파이서닉한 코드(보다 간결하고 가독성이 좋음)라고 추천해 줌. 

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            prev = result[-1]
            row = [1] + [prev[j] + prev[j + 1] for j in range(len(prev) - 1)] + [1]
            result.append(row)
        return result
