import math 

class Solution:
    def __init__(self):
        self.memo = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        if amount < 0:
            return -1
        
        if amount in self.memo:
            return self.memo[amount]
            
        rslt = math.inf
        for x in coins:
            val = self.coinChange(coins, amount-x)
            if val >= 0:
                rslt = min(rslt, val + 1)
        rslt = rslt if rslt < math.inf else -1
        self.memo[amount] = rslt
        return rslt