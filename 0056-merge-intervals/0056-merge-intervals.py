class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:(x[0], x[1]))
        print(intervals)
        stack = []

        for interval in intervals:
            if len(stack) == 0: 
                stack.append(interval)
            
            if stack[-1][1] >= interval[0]:
                stack[-1][1] = max(stack[-1][1], interval[1])
            else:
                stack.append(interval)

        # print(stack)
        return stack

