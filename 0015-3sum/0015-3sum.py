class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)

        rslt = set()
        nums.sort()
        for i in range(0, l):
            target = -nums[i]
            lookup = {}
            for j in range(i+1, l):
                if nums[j] in lookup:
                    rslt.add((nums[i], target - nums[j], nums[j]))
                lookup[target - nums[j]] = j
            
        return list(rslt)