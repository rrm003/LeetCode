class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        rslt = 0

        for x in nums:
            rslt = rslt ^ x

        visited = set()
        for x in nums:
            curr = rslt ^ x
            if curr in visited : return x
            visited.add(curr)

        return rslt