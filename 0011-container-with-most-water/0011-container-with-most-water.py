class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0 
        end = len(height) - 1

        area = 0
        while start < end:
            h = min(height[start], height[end])
            dis = end - start
            area = max(area, h * dis)

            if height[start] < height[end]:
                start+=1
            else:
                end-=1
        
        return area