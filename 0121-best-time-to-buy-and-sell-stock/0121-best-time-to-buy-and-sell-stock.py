from collections import deque 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:       
        stack = deque([])

        rslt = 0
        for x in prices:
            if not stack:
                stack.append(x)
                continue
            
            if stack[-1] > x:
                while stack and stack[-1] > x:
                    stack.pop()
            else:
                rslt = max(rslt, x - stack[0])
            
            stack.append(x)

        return rslt