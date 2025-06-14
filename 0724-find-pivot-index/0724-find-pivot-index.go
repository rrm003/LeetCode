func pivotIndex(nums []int) int {
    total := 0 
    for _, num := range nums {
        total += num
    }   

    prefix := []int{0}

    for i, num := range nums {
        curr_sum :=  prefix[len(prefix) - 1]
        if curr_sum == total - (num + curr_sum) {
            return i
        }

        prefix = append(prefix, curr_sum +  num)
    }   

    return -1
}