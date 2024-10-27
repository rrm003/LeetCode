class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        rslt = []
        intervals.append(newInterval)
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        for interval in intervals:
            if len(rslt) == 0:
                rslt.append(interval)
                continue

            # if rslt[-1][1] >= newInterval[0]:
            #     rslt[-1][1] = max(rslt[-1][1], newInterval[1])
            
            if rslt[-1][1] >= interval[0]:
                rslt[-1][1] = max(rslt[-1][1], interval[1])
            else:
                rslt.append(interval)

        return rslt