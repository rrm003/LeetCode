class Solution:
    def isdigit(self, c) -> bool:
        digits = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        if c in digits:return True
        return False

    def decodeString(self, s: str) -> str:
        stack = []

        i = 0 
        l = len(s)
        while i < l:
            if s[i] != "]":
                stack.append(s[i])
            else:
                rem = "" 
                # extract string
                while stack and stack[-1] != "[":
                    rem = stack[-1] + rem
                    stack = stack[:-1]

                if stack[-1] == "[":
                    stack = stack[:-1]

                num = ""
                # extract num
                while stack and self.isdigit(stack[-1]):
                    num = stack[-1] + num
                    stack = stack[:-1]
                
                # push rslt to stack
                rslt = rem
                if num:
                    reps = int(num)
                    rslt = reps * rslt
                
                stack.append(rslt)
        
            i+=1

        return "".join(stack)


