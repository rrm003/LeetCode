class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        lookup = {}

        for x in time:
            rem = (x % 60)
            if rem not in lookup:
                lookup[rem] = 0
            lookup[rem] += 1
        
        print(lookup)
        rslt = 0
        for key, val in lookup.items():
            if key > 30 : continue
            if key == 0 or key == 30:
                rslt += (val * (val - 1))//2
                continue

            rem = 60 - key
            if rem not in lookup:
                continue
            
            f = lookup[rem]
            # print(key, val, rem, f)
            rslt += (val * f)

        return rslt

# 59: 1
# 58: 1
# 56: 2
# 44: 1
# 39: 1
# 38: 1
# 37: 1
# 24: 1
# 23: 1
# 18: 1
# 17: 1  
# 12: 1
# 0: 1