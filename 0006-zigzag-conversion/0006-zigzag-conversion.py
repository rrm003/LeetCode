class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        pattern = [["" for _ in s] for _ in range(0, numRows)]
        i, j, l= 0, 0, len(s)

        ptr = 0
        while ptr < len(s):
            # traverse down i ++
            while i < numRows and j < l and ptr < l:
                pattern[i][j] = s[ptr]
                ptr += 1
                i += 1

            if ptr >= l : break
            i-=2
            j += 1
            # traverse up daigonally  i--, j++
            while i>=0 and j < l and ptr < l:
                pattern[i][j] = s[ptr]
                ptr += 1
                j += 1
                i -= 1
            
            i+=1
            j-=1
            ptr -= 1

        rslt = ""
        for row in pattern:
            rslt += "".join(row)

        return rslt
