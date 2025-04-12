class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        n = len(nums)
        for i in range(n):
            if i > index: return False
            index = max(i+nums[i], index)

        return True