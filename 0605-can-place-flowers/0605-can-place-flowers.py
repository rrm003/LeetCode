class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 0: False
        if n == 0: return True
        
        l = len(flowerbed)
        if not flowerbed[0] and 1<l:
            flowerbed[0] = 1
            n-=1

        for i in range(1, l):
            if i - 1>= 0 and flowerbed[i] == 0 and i+1 <l:
                if not flowerbed[i-1] and not flowerbed[i+1]:
                    flowerbed[i] = 1
                    n-=1
                
                if n == 0: break
            
            i+=1

        if n > 0 :
            if not flowerbed[l-1] and l-2>=0 and not flowerbed[l-2]:
                flowerbed[l-1] = 1
                n -= 1

        return n==0

        
