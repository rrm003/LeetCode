class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        prev = -math.inf
        i = 0
        while i < len(nums) - 1:
            if nums[i] > prev and nums[i] > nums[i+1]:
                return i

            prev = nums[i]
            i += 1
        
        if nums[i] > nums[i-1]:
            return nums[i]
        
        return 0
