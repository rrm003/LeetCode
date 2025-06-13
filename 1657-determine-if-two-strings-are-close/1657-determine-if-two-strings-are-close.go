func getFreqMap[T comparable](arr []T) map[T]int{
    lookup := make(map[T]int)

    for _, n := range arr {
        if _, ok := lookup[n]; !ok{
            lookup[n] = 0
        }

        lookup[n] += 1
    }

    return lookup
}

func closeStrings(word1 string, word2 string) bool {
    if len(word1) != len(word2) {
        return false
    }

    lookup1 := getFreqMap([]rune(word1))
    lookup2 := getFreqMap([]rune(word2))

    if len(lookup1) != len(lookup2) {
        return false
    }

    for k, _ := range lookup1 {
        if _, ok := lookup2[k]; !ok {
            return false
        }
    }

    f1 := []int{}
    for _, v := range lookup1{
        f1 = append(f1, v)
    }

    f2 := []int{}
    for _, v := range lookup2{
        f2 = append(f2, v)
    }

    freqfreq1 := getFreqMap(f1)
    freqfreq2 := getFreqMap(f2)

    if len(freqfreq1) != len(freqfreq2) {
        return false
    }

    for k, v := range freqfreq1 {
        if v != freqfreq2[k] {
            return false
        }
    }

    return true
}