class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        l = len(nums)

        i = 0
        for i in range(l): 
            if nums[i] in lookup:
                return [lookup[nums[i]], i]

            lookup[target - nums[i]] = i 
            
        return []