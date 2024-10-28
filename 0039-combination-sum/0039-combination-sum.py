class Solution:
    def find(self, candidates, i, stack, target, result):
        if target < 0 : return []
        if target == 0 :
            result.append(stack)  
            return stack
        
        for j in range(i, len(candidates)):
            s = stack.copy()
            s.append(candidates[j])
            score = target - candidates[j]
            rslt = self.find(candidates, j, s, score, result)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        for i, candidate in enumerate(candidates):
            stack = []
            stack.append(candidate)
            score = target - candidate
            rslt = self.find(candidates, i, stack, score, result)
            stack = stack[:-1]

        return result