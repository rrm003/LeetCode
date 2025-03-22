class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        stock = []

        for price in prices:
            if len(stock) == 0:
                stock.append(price)
                continue
            
            while stock and stock[-1] > price:
                stock = stock[:-1]
            
            if stock:
                max_profit = max(max_profit, price - stock[0])
            
            stock.append(price)
        
        return max_profit