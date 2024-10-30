class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Approach 1: hashmap 

            1. use the map to keep the value and its index mapping
            2. iterate over each element
                2.1 check if the diff exists in the map
                    if exists 
                        return diff value from map and current index
                2.2 add current value as key and current index as value in map
            3. if no pair found return [], but as given the pair will exits this step will never execute

        Time complexity : O(n)  // iterate over all n elements
        Space Complexity: O(n)  // need to store n elements in the map

        Another Approach : Two Pointer
        '''
        lookup = {}

        for i, x in enumerate(nums):
            diff = target - x
            if diff in lookup:
                return [lookup[diff], i]
            
            lookup[x] = i
        
        return []
