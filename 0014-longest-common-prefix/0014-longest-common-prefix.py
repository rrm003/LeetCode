class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l  = len(strs)
        word_len = len(strs[0])

        i = 0
        rslt = ""
        while i < word_len:
            c = 0 
            char = strs[0][i]
            for word in strs[1:]:
                if i < len(word) and word[i] == char:
                    c+=1
                else:
                    return rslt
            
            rslt += char
            i+=1
        
        return rslt