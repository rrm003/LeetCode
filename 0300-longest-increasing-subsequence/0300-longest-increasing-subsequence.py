class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [1 for i in range(l)]

        j = 0
        i = j + 1

        while i < l:
            j = 0
            while j < i:
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                j+=1
            
            i += 1
        print(dp)

        return max(dp)