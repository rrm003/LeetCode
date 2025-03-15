class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)

        ps = 0
        pt = 0

        while ps < ls and pt < lt:
            if s[ps] == t[pt]:
                ps += 1
                pt += 1
            elif s[ps] != t[pt]:
                pt += 1
        
        return ps == ls 