class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = 0 
        j = 0
        
        g.sort()
        s.sort()

        count = 0
        for i, child in enumerate(g):
            while j < len(s) and child > s[j]:
                j+=1
            
            if j < len(s) and child <= s[j]:
                count += 1
            
            j+=1
        
        return count