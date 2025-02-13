class Solution:
    def merge(self, interval: List[List[int]]) -> List[List[int]]:
        interval.sort(key=lambda x : (x[0],x[1]))
        rslt = []
        i = 0
        print(interval)
        for i in range(len(interval)):
            if len(rslt) == 0: 
                rslt.append(interval[i])
                i += 1
                continue
            
            if interval[i][0] <= rslt[-1][1]:
                rslt[-1][1] = max(interval[i][1], rslt[-1][1])
            
            else:
                rslt.append(interval[i])
            
            i += 1

        return rslt