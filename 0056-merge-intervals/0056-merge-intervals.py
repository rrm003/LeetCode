class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:(x[0], x[1]))

        rslt = []
        for interval in intervals:
            if len(rslt) == 0:
                rslt.append(interval)
                continue
            
            if rslt[-1][1] >= interval[0]:
                rslt[-1][1] = max(rslt[-1][1], interval[1])
            else:
                rslt.append(interval)
        
        return rslt