class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        rslt = set()
        lookup = {}
        window = 10 # given in problem

        i = 0
        while i <= len(s) - window:
            print(i, i + window)

            curr = s[i : i + window]
            if curr not in lookup:
                lookup[curr] = 0

            lookup[curr] += 1
            if lookup[curr] > 1:
                rslt.add(curr)
            
            i+=1

        return list(rslt)
        