class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value=prices[0]
        max_profit=0
        for i in range (len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]
            else:
                profit=prices[i]-min_value
                if profit> max_profit:
                     max_profit = profit
        return max_profit     

