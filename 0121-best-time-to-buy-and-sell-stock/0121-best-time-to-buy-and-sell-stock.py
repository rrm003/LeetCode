class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyAt = prices[0]

        for price in prices[1:]:
            profit = max(profit, price - buyAt)
            buyAt = min(buyAt, price)
        
        return profit