class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)

        if abs(l1 - l2) > 2: return False

        if l1 == l2:
            miss = 0 
            i = 0 
            while i < l1:
                if s[i] != t[i]:
                    miss+=1
                i+=1

            return miss == 1
        
        a, b = 0, l1 - 1
        x, y = 0, l2 - 1

        m1 = 0
        while a < l1 and x < l2 and s[a] == t[x]:
            m1 += 1
            a+=1
            x+=1
        
        m2 = 0
        while b>= 0 and y>=0 and s[b] == t[y]:
            m2 += 1
            b-=1
            y-=1
        
        m = max(l1, l2)

        return m1 + m2 + 1 == m or m1 + m2 + 2 == m * 2

        