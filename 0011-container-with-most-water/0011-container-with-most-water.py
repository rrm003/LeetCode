class Solution:
    def maxArea(self, height: List[int]) -> int:
        s = 0
        e = len(height) -1

        rslt = 0

        while s < e:
            h = min(height[s], height[e])
            w = e-s
            rslt = max(rslt, h * w)

            if height[s] < height[e]:
                s+=1
            elif height[s] > height[e]:
                e-=1
            else:
                s+=1
                e-=1
        
        return rslt