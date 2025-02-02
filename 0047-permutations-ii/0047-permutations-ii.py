class Solution:
    def permute(self, input, output, rslt):
        if len(input) == 0:
            rslt.append(output)
            return 

        visited = set()
        for i, x in enumerate(input):
            if x in visited:
                continue
            
            visited.add(x)
            new_output = output.copy()
            new_output.append(x)
            self.permute(input[:i] + input[i+1:], new_output, rslt)
        


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        rslt = []
        self.permute(nums, [], rslt)
        return rslt        
