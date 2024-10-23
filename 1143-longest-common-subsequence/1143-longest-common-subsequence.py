class Solution:
    def __init__(self):
        self.memo = {}

    def lcs(self, text1, text2, i, j):
        key = f"{i},{j}"
        if key in self.memo:
            return self.memo[key]

        if i == len(text1) or j == len(text2):
            return 0
        elif text1[i] == text2[j]:
            self.memo[key] = 1+self.lcs(text1, text2, i+1, j+1)
            return self.memo[key]
        else:
            self.memo[key] = max(self.lcs(text1, text2, i+1, j), self.lcs(text1, text2, i, j+1))
            return self.memo[key]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.lcs(text1, text2, 0, 0)