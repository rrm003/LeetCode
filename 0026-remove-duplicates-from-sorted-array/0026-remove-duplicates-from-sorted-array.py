class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0 
        i = 0  
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1

            nums[p] = nums[i]
            p+=1

            i = j

        return p