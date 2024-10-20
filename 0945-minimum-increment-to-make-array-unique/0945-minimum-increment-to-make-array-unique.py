class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        m = max(nums)
        freq = [0] * (m + len(nums)) 

        for x in nums:
            freq[x] += 1
        
        moves = 0
        for i, v in enumerate(freq):
            extra = v - 1
            if extra < 0: continue

            moves += extra
            if i < len(freq)-1:
                freq[i+1] += extra
            freq[i] -= 1

        return moves