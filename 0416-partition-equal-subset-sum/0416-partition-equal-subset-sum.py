class Solution:
    def partition(self, open :List[int], i :int, total, dp) -> bool:
        if i == len(open): return False
        if total == 0: return True

        if dp[i][total] != -1: return dp[i][total]

        rslt = False
        rslt = rslt or self.partition(open, i + 1, total, dp)
    
        rslt = rslt or self.partition(open, i + 1, total - open[i], dp)
        
        dp[i][total] = rslt
        return rslt


    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        dp = [[-1 for x in range(total//2 + 1)] for y in range(len(nums))]
        return self.partition(nums, 0, total//2, dp)
