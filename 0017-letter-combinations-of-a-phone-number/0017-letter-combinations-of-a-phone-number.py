class Solution:
    def __init__(self):
        self.lookup = {
                '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z'],
        }

    def solve(self, digits, prefix, rslt):
        if len(digits) == 0:
            if len(prefix) > 0:
                rslt.append(prefix)
            return 
        
        curr = digits[0]
        digits = digits[1:]

        for x in self.lookup[curr]:
            self.solve(digits, prefix + x, rslt)
        


    def letterCombinations(self, digits: str) -> List[str]:
        rslt = []
        self.solve(digits, "", rslt)
        return rslt