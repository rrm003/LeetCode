class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [x for x in nums[-2::-1]]
        print(stack)

        i = len(nums) -1
        while i > -1:
            while len(stack) > 0 and stack[-1] <= nums[i]:
                stack = stack[:-1]
            
            x = nums[i]
            if len(stack) > 0:
                nums[i] = stack[-1]
            else:
                nums[i] = -1
            
            stack.append(x)
            i-=1
 
        return nums