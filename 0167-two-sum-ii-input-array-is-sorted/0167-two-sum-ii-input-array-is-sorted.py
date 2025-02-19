class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        s = 0
        e = l - 1

        while s < e and s < l and e > 0:
            sum = nums[s] + nums[e]
            if sum == target:
                return [s+1, e+1]

            elif sum > target:
                e -=1
            
            else: 
                s += 1

        return rslt