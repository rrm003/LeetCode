class Solution:
    def trap(self, height: List[int]) -> int:
        height_left = [-math.inf for _ in height]
        height_right = [-math.inf for _ in height]
        l = len(height)

        val = 0
        for i in range(l):
            val = max(height[i], val)
            height_right[i] = val
        
        val = 0 
        j = l - 1
        while j >= 0:
            val = max(height[j], val)
            height_left[j] = val
            j -= 1
        

        water = 0
        for i in range(l):
            m = min(height_left[i], height_right[i])
            water += m - height[i]

        return water
        

                