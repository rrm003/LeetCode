class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0 
        l = len(chars)
        curr = 0
        while i < l:
            chars[curr] = chars[i]
            curr += 1
            j = i + 1
            while j < l and chars[j] == chars[i]:
                j+=1
            
            if j - i > 1: 
                for x in str(j-i):
                    chars[curr] = x
                    curr += 1
            i = j

        return curr