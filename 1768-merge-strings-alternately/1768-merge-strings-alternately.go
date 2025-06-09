func mergeAlternately(word1 string, word2 string) string {
    var merged = ""

    var i, j = 0, 0
    var l1, l2 = len(word1), len(word2)

    for i < l1 && j < l2{
        merged = merged + string(word1[i])
        merged = merged + string(word2[j])
        i += 1
        j += 1
    }

    for i < l1{
        merged += string(word1[i])
        i += 1
    }

    for j < l2 {
        merged += string(word2[j])
        j += 1
    }

    return merged
}