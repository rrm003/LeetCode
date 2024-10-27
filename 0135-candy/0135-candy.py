class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        rslt  = [1] * l

        for i in range(1, l):
            if ratings[i-1] < ratings[i]:
                rslt[i] = rslt[i-1] + 1
        
        for i in range(l-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                rslt[i] = max(rslt[i], rslt[i+1]+1)
        
        return sum(rslt)