class Solution:
    def trap(self, height: List[int]) -> int:
        left_stack = []
        right_stack = []

        m = 0
        for x in height:
            left_stack.append(m)
            m = max(m, x)
            
        m = 0
        for x in height[::-1]:
            right_stack.append(m)
            m = max(m, x)
        
        right_stack.reverse()
        # print(height)
        # print(left_stack)
        # print(right_stack)

        cap = 0
        for i, h in enumerate(height):
            cap += max(0, min(left_stack[i], right_stack[i]) - h)

        return cap