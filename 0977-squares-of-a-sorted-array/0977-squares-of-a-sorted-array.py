import heapq as hq

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [nums[0] * nums[0]]

        neg_index = 0 
        pos_index = 0
        l = len(nums)

        while neg_index < l and nums[neg_index]<0:
            neg_index += 1
        
        pos_index = neg_index
        neg_index -= 1

        rslt = []
        while neg_index >=0 or pos_index < l:
            if neg_index >=0 and pos_index < l and -nums[neg_index] <= nums[pos_index]:
                sq = -nums[neg_index] * -nums[neg_index]
                rslt.append(sq)
                neg_index -= 1
            elif neg_index >=0 and pos_index < l and -nums[neg_index] > nums[pos_index]:
                sq = nums[pos_index] * nums[pos_index]
                rslt.append(sq)
                pos_index += 1
            elif neg_index >=0 :
                sq = -nums[neg_index] * -nums[neg_index]
                rslt.append(sq)
                neg_index -= 1
            elif pos_index <l:
                sq = nums[pos_index] * nums[pos_index]
                rslt.append(sq)
                pos_index += 1
        
        return rslt