class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)

        rslt = ""
        i = 0   # word1 index  
        j = 0   # word2 index

        while i < l1 and j < l2:
            rslt += word1[i]
            rslt += word2[j]
            i+=1
            j+=1
        
        while i < l1:
            rslt += word1[i]
            i+=1
        
        while j < l2:
            rslt += word2[j]
            j += 1
        
        return rslt