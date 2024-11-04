class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        candies = [1] * l

        i = 1
        while i < l:
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

            i+=1
        
        print(candies)

        i = l-2

        while i >=0:
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

            i-=1
        
        print(candies)

        return sum(candies)
        
