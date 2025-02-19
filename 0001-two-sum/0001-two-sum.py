class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in lookup:
                return [lookup[diff], i]

            if x not in lookup:
                lookup[x] = i

        return []