class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f = float('inf')
        s = float('inf')

        for x in nums:

            if x <= f:
                f = x
            elif x <= s:
                s = x
            else:
                return True
        
        return False