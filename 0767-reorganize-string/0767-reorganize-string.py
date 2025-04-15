import heapq as hq

class Char:
    def __init__(self, k, v):
        self.k = k
        self.f = v

    def __repr__(self):
        return f"({self.k}, {self.f})"
    
    def __lt__(self, obj):
        return obj.f < self.f

class Solution:
    def reorganizeString(self, s: str) -> str:
        lookup = {}
        for ch in s:
            if ch not in lookup:
                lookup[ch] = 0
            lookup[ch] += 1
        
        ch_freq = []
        for k, v in lookup.items():
            ch_freq.append(Char(k, v))

        hq.heapify(ch_freq)
        print(ch_freq)
        rslt = ""

        while ch_freq:
            char = hq.heappop(ch_freq)
            ch, f = char.k, char.f

            if len(rslt) > 0 and rslt[-1] == ch and ch_freq:
                next = hq.heappop(ch_freq)
                rslt += next.k
                if next.f - 1>0:
                    hq.heappush(ch_freq, Char(next.k, next.f-1))
            elif rslt == "" or ch != rslt[-1]:
                rslt += ch
                f -= 1
            else:
                break
                 
            if f>0: 
                hq.heappush(ch_freq, Char(ch, f))
        
        print(rslt)
        if len(rslt) != len(s): return ""
        
        return rslt