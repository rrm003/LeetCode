func largestAltitude(gain []int) int {
    prefix := []int{0}

    for _, val := range gain {
        g := val + prefix[len(prefix) - 1]
        prefix = append(prefix, g)
    }  

    fmt.Println(prefix)

    return int(slices.Max(prefix))
}