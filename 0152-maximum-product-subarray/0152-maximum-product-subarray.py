class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        high = nums[0]
        low = nums[0]
        product = nums[0]

        for i in range(1, n):
            curr = nums[i]
            if curr < 0:
                high, low = low, high
            
            high = max(curr, high * curr)
            low = min(curr, low * curr)
            product = max(product, high)
        
        return product