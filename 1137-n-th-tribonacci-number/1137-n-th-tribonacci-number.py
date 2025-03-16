class Solution:
    def prev(self, n, dp):
        if n < 1 : return 0
        if n == 1 : return 1
        if n in dp : return dp[n]

        tn = self.prev(n-1, dp)
        tn2 = self.prev(n-2, dp)
        tn3 = self.prev(n-3, dp)
        
        dp[n] = tn+tn2+tn3

        return dp[n]

    def tribonacci(self, n: int) -> int:
        dp = {}
        return self.prev(n, dp)