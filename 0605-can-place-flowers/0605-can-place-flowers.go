func canPlaceFlowers(flowerbed []int, n int) bool {
    l := len(flowerbed)

    if n == 0 {return true} 

    for i:=0; i<l; i++ {

        if flowerbed[i]==0 { 
            left_empty := (i==0 || (i-1>=0 && flowerbed[i - 1]==0))
            right_empty := (i==l-1 || (i+1<l && flowerbed[i+1]==0)) 
            
            if left_empty && right_empty{
                flowerbed[i] = 1
                n -= 1
            } 
        }
    }   

    return n <= 0
}