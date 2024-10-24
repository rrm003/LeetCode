
func lis(arr []int, index int, lookup map[int]int) int {
	rslt := 0
	for i := index + 1; i < len(arr); i++ {
		if arr[i] > arr[index] {
            if val, ok := lookup[i]; ok{
                rslt = max(rslt, val)
                continue
            }

			lookup[i] = 1+lis(arr, i, lookup)
            rslt = max(rslt, lookup[i])
		}
	}

	return rslt
}

func lengthOfLIS(arr []int) int {
    rslt := 0
    lookup := map[int]int{}

	for i := len(arr)-1; i >= 0; i-- {
        if val, ok := lookup[i]; ok{
            rslt = max(rslt, val)
            continue
        }

        lookup[i] = 1+lis(arr, i, lookup)
        rslt = max(rslt, lookup[i])
	}

	// fmt.Println(rslt)
    return rslt
}