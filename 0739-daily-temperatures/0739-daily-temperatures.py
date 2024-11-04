class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rslt = []
        stack = []
        l = len(temperatures)
        
        i = l-1
        while i >= 0:
            if len(stack) == 0:
                stack.append(i)
                rslt.append(0)
                i -= 1
                continue
            
            while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack = stack[:-1]
            
            if len(stack) > 0:
                rslt.append(stack[-1] - i)
            else:
                rslt.append(0)
            
            stack.append(i)
            i-=1
        
        rslt.reverse()
        
        return rslt
