import math

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = 0 

        min_dist = 0
        rslt = []
        while i < k:
            min_dist += abs(x-arr[i])
            i+=1
        
        rslt = arr[:k]
        print(rslt)

        i=1
        dist = min_dist
        while i <= len(arr) - k:
            print(min_dist, dist)
            dist -= abs(x - arr[i-1])
            dist += abs(x - arr[i+k-1])

            if dist < min_dist:
                min_dist = dist
                rslt = arr[i:i+k]
            
            i+=1
        
        return rslt
                                                                                                                                         