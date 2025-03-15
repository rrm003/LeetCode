class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ones = 1
        flag = False

        i = 0
        j = 0

        rslt = 0
        while j < len(nums):
            if nums[j] == 0 and ones == 0:
                k = i
                rslt = max(rslt, j - i)
                while k<j and nums[k] != 0:
                    k+=1
                
                if k<j and nums[k] == 0:
                    i = k+1

            elif nums[j] ==0 and ones == 1:
                flag = True
                ones = 0
            
            j+=1
        
        rslt = max(rslt, j - i)
        # if not flag: rslt - 1

        return rslt - 1


