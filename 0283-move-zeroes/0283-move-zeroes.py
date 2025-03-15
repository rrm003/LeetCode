class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = len(nums)
        zeros = 0 
        for x in nums:
            if x == 0 : zeros+=1
        
        curr = 0 
        i = 0
        while i < l:
            if nums[i] != 0:
                nums[curr] = nums[i]
                curr+=1
            
            i+=1

        while zeros:
            nums[l - zeros] = 0
            zeros -= 1
        