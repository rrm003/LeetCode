class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = {}
        stack = []
        nums2.reverse()
        for x in nums2:
            if len(stack) == 0:
                lookup[x] = -1
                stack.append(x)
                continue
            
            lookup[x] = -1
            while len(stack) > 0 and stack[-1] < x:
                stack = stack[:-1]

            if len(stack) > 0:
                lookup[x] = stack[-1]

            stack.append(x)
        
        print(lookup)

        rslt = []
        for x in nums1:
            rslt.append(lookup[x])

        return rslt


