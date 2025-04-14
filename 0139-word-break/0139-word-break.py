class Solution:
    def dfs(self, s: str, i: int, lookup, memo) -> bool:
        if i == len(s): return True
        if i in memo: return memo[i]

        ch = s[i]
        if ch not in lookup:
            memo[i] = False
            return False

        for word in lookup[ch]:
            l = len(word) 
            if i+l <= len(s) and s[i:i+l] == word:
                rslt =  self.dfs(s, i+l, lookup, memo)
                memo[i] = rslt
                if rslt : return True
        
        memo[i] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lookup = {}
        for word in wordDict:
            if word[0] not in lookup:
                lookup[word[0]] = []

            lookup[word[0]].append(word)
        
        memo = {}
        return self.dfs(s, 0, lookup, memo)
