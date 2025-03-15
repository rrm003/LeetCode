class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        rslt = ""
        for word in words[::-1]:
            if word: rslt += " " + word
        
        return rslt[1:]