class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        smallest = math.inf
        l = len(nums)-1

        nums.sort()

        for i, x in enumerate(nums[:-2]):
            j = i + 1
            k = l

            rem = target - nums[i]
            while j < k :
                s = nums[j] + nums[k]
                diff = rem - s 
                if smallest < 0 and diff < 0:
                    smallest = max(smallest, diff)
                else:
                    smallest = min(smallest, diff)

                print(smallest)

                if s == rem:
                    break
                
                if s > rem:
                    k-=1
                else:
                    j+=1
        
        return target - smallest
                