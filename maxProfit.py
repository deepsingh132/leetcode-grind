from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range (1, len(prices)): # start from the second day/element for comparing with the previous day/element
            if prices[i] > prices[i - 1]: # if the current day's price is greater than the previous day's price
                profit += prices[i] - prices[i - 1] # Sell the stock and add the difference to the profit
        return profit

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))