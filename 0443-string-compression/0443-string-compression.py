class Solution:
    def compress(self, chars: List[str]) -> int:
        rslt = []

        i = 0
        p = 0
        l = len(chars)

        while i < l:
            curr = chars[i]
            count = 1

            j = i + 1
            while j < l and curr == chars[j]:
                count+=1
                j += 1

            chars[p] = curr
            p += 1
            if count > 1: 
                freq = str(count)
                for f in freq:
                    chars[p] = f
                    p += 1

            i = j
        
        return p