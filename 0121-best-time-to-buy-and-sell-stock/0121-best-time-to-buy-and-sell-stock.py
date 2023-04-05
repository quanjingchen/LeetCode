class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        maxProfit = 0
        for i, price in enumerate(prices):
            if price < prices[low]:
                low = i
            if price - prices[low] > maxProfit:
                maxProfit = price - prices[low] 
        return maxProfit
                
            
            
        