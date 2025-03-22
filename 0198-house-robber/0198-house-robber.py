class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1: return nums[0]

        house = [0 for i in range(l)]

        house[0] = nums[0]
        house[1] = max(house[0], nums[1])
        
        for i in range(1, l):
            house[i] = max(nums[i] + house[i-2], house[i-1])

        print(house)

        return house[-1]