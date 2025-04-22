class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        stack.append(prices[0])
        
        profit = 0
        for price in prices[1:]:
            while stack and stack[-1] > price:
                stack = stack[:-1]
            
            if stack:
                profit = max(profit, price - stack[0])
            
            stack.append(price)
        
        # print(stack)

        return profit