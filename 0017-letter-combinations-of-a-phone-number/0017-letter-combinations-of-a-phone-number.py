class Solution:
    def combine(self, digit, lookup):
        if not digit: return []

        curr = digit[0]
        digit = digit[1:]
        combinations = self.combine(digit, lookup)
        if not combinations:
            return lookup[curr]
        else:
            rslt = []
            for i in lookup[curr]:
                for combination in combinations:
                    rslt.append(i + combination)
            
            return rslt
        
        return []

    def letterCombinations(self, digits: str) -> List[str]:
        lookup = {
            "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
            "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"],
        }

        return self.combine(digits, lookup)