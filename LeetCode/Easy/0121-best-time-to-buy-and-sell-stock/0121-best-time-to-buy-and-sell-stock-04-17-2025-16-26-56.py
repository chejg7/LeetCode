class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

# 최초에 작성했던 코드는 시간 효율성이 O(n2)으로 실패함. 이 문제를 효율적으로 풀기 위해서는 각 요소를 한번씩만 확인하면서 최솟값을 기준으로 최대의 차이를 가지는 값만 찾아내면 됨. 

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profits = []
#         for i in range(len(prices)):
#             max_profits.append(max(prices[i:]) - prices[i])  

#         return max(max(max_profits), 0)
