class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        rslt = set()
        for i, first in enumerate(nums[:-1]):
            rem = target - first
            
            lookup = {}
            for j in range(i+1, len(nums)):
                third = nums[j]
                diff = rem - third
                if diff in lookup:
                    grp = [first, diff, third]
                    grp.sort()
                    rslt.add(tuple(grp))
                
                lookup[third] = i
            
        return list(rslt)