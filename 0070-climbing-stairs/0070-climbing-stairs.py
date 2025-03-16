class Solution:
    def climb(self, n: int, dp):
        if n < 0 : return 0
        if n ==0 : return 1
        if n in dp: return dp[n]

        rslt = 0
        rslt += self.climb(n-1, dp)
        rslt += self.climb(n-2, dp)
        dp[n] = rslt

        return rslt

    def climbStairs(self, n: int) -> int:
        dp = {}
        return self.climb(n, dp)