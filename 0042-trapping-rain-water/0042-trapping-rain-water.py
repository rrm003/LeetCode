class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        left = [-math.inf for _ in range(l)]
        right = [-math.inf for _ in range(l)]

        i = 0 
        val = 0
        while i < l:
            val = max(height[i], val)
            left[i] = val
            i+=1
        
        j = l - 1
        val = 0
        while j>=0 :
            val = max(height[j], val)
            right[j] = val
            j -= 1
        
        rslt = 0
        for i in range(l):
            h = min(left[i], right[i])
            rslt += h - height[i]

        return rslt