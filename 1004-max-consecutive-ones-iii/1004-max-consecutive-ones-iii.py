class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0 

        rslt = 0
        while end < len(nums):
            if nums[end] == 1 or (nums[end] == 0 and k > 0):
                if nums[end] == 0:
                    k -= 1
                end += 1
            else:
                rslt = max(rslt, end - start)
                if nums[start] == 0: 
                    k+=1
                start+=1

        rslt = max(rslt, end - start)
        return rslt