class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rslt = 0
        stack = []

        for p in prices:
            if len(stack) == 0:
                stack.append(p)
                continue
            
            elif stack[-1] < p:
                rslt = max(rslt, p-stack[0])
            
            elif stack[-1] > p:
                while len(stack)>0 and stack[-1] > p:
                    stack = stack[:-1]
                
                stack.append(p)
                rslt = max(rslt, p-stack[0])
        
        return rslt