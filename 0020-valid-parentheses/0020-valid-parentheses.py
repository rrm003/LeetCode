from collections import deque as dq

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False

        brackets = {")":"(", "]":"[", "}":"{"}

        stack = deque([])
        for b in s:
            if b in brackets.values():
                stack.append(b)
            else:
                if len(stack) == 0: return False
                if stack[-1] != brackets[b]: return False
                stack.pop()
        
        return len(stack) == 0