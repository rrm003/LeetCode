class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = len(nums)
        prefix = [None] * l
        rslt = 0

        lookup = {0: 1}
        prefix[0] = nums[0]
        lookup[prefix[0]] = 0
        if prefix[0] == k:
            rslt += 1

        i = 1
        while i < l :
            print(i, rslt)
            prefix[i] = prefix[i-1] + nums[i]
            if prefix[i] - k in lookup:
                rslt += 1            
            lookup[prefix[i]] = i
            i += 1
        
        print(prefix)

        return rslt

