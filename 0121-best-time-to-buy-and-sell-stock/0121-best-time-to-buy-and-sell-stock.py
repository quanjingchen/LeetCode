class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, high = 0, 0
        maxProfit = 0
        for i, price in enumerate(prices):
            if price < prices[low]:
                low = i
            elif price > prices[high]:
                high = i
            if low > high:
                high = low
            if prices[high] - prices[low] > maxProfit:
                maxProfit = prices[high] - prices[low] 
        return maxProfit
                
            
            
        