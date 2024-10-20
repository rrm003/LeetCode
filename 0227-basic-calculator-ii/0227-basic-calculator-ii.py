class Solution:
    def calculate(self, s: str) -> int:
        digits = [str(x) for x in range(0, 10)]
        operators = ["+", "-", "*", "/"]
        expresion = []

        i=0
        while i < len(s):
            if s[i] in operators:
                expresion.append(s[i])
            elif s[i] in digits:
                digit = 0 
                while i < len(s) and s[i] in digits:
                    digit = digit * 10 + int(s[i])
                    i+=1

                i -= 1
                expresion.append(digit)
            
            i+=1
        
        print(expresion)

        stack = []
        stack.append(expresion[0])
        i=1
        while  i < len(expresion):
            x = expresion[i]
            if x in ["*", "/"]:
                r = stack[-1] * expresion[i+1] if x =="*" else stack[-1] // expresion[i+1]  
                stack = stack[:-1]
                stack.append(r)
                # print(r)
                i+=1
            else: 
                stack.append(x)
            
            i+=1

        # print(stack)
        rslt = stack[0]
        i = 1
        while i < len(stack):
            rslt = rslt + stack[i+1] if stack[i] =="+" else rslt - stack[i+1]
            i+=2

        print(rslt)
        return int(rslt)
            
