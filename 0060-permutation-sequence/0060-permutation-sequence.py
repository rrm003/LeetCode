class Solution:
    def permute(self, input, output, k , rslt) -> []:
        if len(input) == 0:
            rslt.append(output)
            rslt_str = ""
            if len(rslt) == k:
                for x in rslt[k-1]:
                    rslt_str += str(x)
            return rslt_str
        
        for i, val in enumerate(input):
            o1 = output.copy()
            o1.append(val)
            p = self.permute(input[:i]+input[i+1:], o1, k, rslt)
            if p != "": return p

        return ""

    def getPermutation(self, n: int, k: int) -> str:
        input = [x+1 for x in range(n)]
        rslt = []
        return self.permute(input, [], k, rslt)
