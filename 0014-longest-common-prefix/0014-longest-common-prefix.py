class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        l = len(strs)
        if l <= 1: return strs[0]

        prefix = ""
        while i < 200:
            count = 0
            for j in range(l - 1):
                if i >= len(strs[j]) or i >= len(strs[j+1]): return prefix
                if strs[j][i] != strs[j+1][i]: return prefix
                count += 1

            if count == l- 1:
                prefix += strs[0][i]
            else: 
                break

            i+=1
        return prefix