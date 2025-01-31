class Solution:
    def iterate(self, input: List[int], output: List[int], rslt: List[int]):
        if len(input) == 0:
            rslt.append(output)
            return
        
        for i, val in enumerate(input):
            new_input = input.copy()
            new_output  = output.copy()

            new_input.pop(i)
            new_output.append(val)
            self.iterate(new_input, new_output, rslt)
        
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        rslt = []
        self.iterate(nums, [], rslt)
        return rslt