class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            prev = merged[-1][1]
            if prev >= start:
                end = max(prev, end)
                merged[-1][1] = end
            else:
                merged.append([start, end])
        
        return merged