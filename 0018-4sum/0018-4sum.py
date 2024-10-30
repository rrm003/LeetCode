class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        rslt = set()
        l = len(nums)

        for i, o in enumerate(nums[:-3]):
            rem1 = target - o
            for j in range(i + 1, l-2):
                rem2 = rem1 - nums[j]

                k = j+1
                m = l-1
                while k < m:
                    s = nums[k] + nums[m]
                    if s == rem2:
                        rslt.add(tuple([o, nums[j], nums[k], nums[m]])) 
                        k+=1
                        m-=1
                    elif s > rem2:
                        m-=1
                    else:
                        k+=1
        
        return list(rslt)
                    