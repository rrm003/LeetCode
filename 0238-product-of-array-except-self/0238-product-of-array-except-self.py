class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        non_zero_prod = 1
        has_zero = False
        has_more_zero = False
        for x in nums:
            if not x and has_zero: has_more_zero = True
            if not x and not has_zero: has_zero = True
            if has_more_zero: return [0] * len(nums)
            if x: non_zero_prod *= x
        
        rslt = []
        for x in nums:
            if x and not has_zero: 
                rslt.append(non_zero_prod // x)
            elif x and has_zero:
                rslt.append(0)
            elif not x:
                rslt.append(non_zero_prod)
        
        return rslt