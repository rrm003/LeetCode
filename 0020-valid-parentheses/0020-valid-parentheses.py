class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {")": "(", "}": "{", "]":"["}

        for ch in s:
            if ch in lookup and stack:
                if stack[-1] != lookup[ch]:
                    return False
                else:
                    stack = stack[:-1]
            else:
                stack.append(ch)

        if len(stack) > 0: return False

        return True