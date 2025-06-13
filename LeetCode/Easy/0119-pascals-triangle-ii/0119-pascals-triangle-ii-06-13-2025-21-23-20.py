class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # result = [[1]]
        # for i in range(1, rowIndex + 1):
        #     temp = []
        #     for j in range(i + 1):
        #         if j == 0 or j == i:
        #             temp.append(1)
        #         else:
        #             temp.append(result[i - 1][j - 1] + result[i - 1][j])
        #     result.append(temp)

        # return result[-1]

        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        return row