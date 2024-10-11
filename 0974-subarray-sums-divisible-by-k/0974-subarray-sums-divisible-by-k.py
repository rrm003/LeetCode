class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total = 0 
        
        lookup = {0: [1]}
        count = 0  

        for i, v in enumerate(nums):
            total += v
            rem = total % k 
            if rem not in lookup:
                lookup[rem] = [i]
            else:
                count += len(lookup[rem])
                lookup[rem].append(i)
        
        return count

            