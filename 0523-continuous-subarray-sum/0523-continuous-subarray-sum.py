class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        lookup = {0: -1}

        total = 0
        for i, v in enumerate(nums):
            total += v
            rem = total % k

            if rem not in lookup:
                lookup[rem] = i
            elif i - lookup[rem] >= 2:
                return True


        return False