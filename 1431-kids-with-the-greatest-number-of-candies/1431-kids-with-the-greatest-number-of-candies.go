func kidsWithCandies(candies []int, extraCandies int) []bool {
    l := len(candies)

    greatest := slices.Max(candies)
    rslt := make([]bool, l)
    
    for i:=0; i<l; i++ {
        total := candies[i] + extraCandies
        if total >= greatest{
            rslt[i] = true
        }else{
            rslt[i] = false
        }
    }

    return rslt
}