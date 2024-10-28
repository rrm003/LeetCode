class Solution:
    def LIS(self, nums, pos, memo) -> int:
        if pos == len(nums): return 0

        rslt = 0

        for i in range(pos+1, len(nums)):
            if nums[pos] < nums[i]:
                if i in memo:
                    rslt = max(rslt, memo[i])
                    continue

                memo[i] = 1+self.LIS(nums, i, memo)
                rslt = max(rslt, memo[i])
            
            # rslt = max(rslt, self.LIS(nums, i, memo))
        
        memo[pos] = rslt
        
        return rslt

    def lengthOfLIS(self, nums: List[int]) -> int:
        rslt = 0
        memo = {}
        
        i = len(nums)-1
        while i >= 0:
            if i in memo:
                rslt = max(rslt, memo[i])
                i-=1
                continue

            memo[i] =  1 + self.LIS(nums, i, memo)
            rslt = max(rslt, memo[i])
            i -= 1

        return rslt