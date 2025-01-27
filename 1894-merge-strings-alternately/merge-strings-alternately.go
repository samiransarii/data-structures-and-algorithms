func mergeAlternately(word1 string, word2 string) string {
    p1 := 0
    p2 := 0

    output := ""
    // merges both the string until the end of the shorter string
    for p1 < len(word1) && p2 < len(word2) {
        output += (string(word1[p1]) + string(word2[p2]))

        p1 += 1
        p2 += 1
    }

    // Merge the remaining string from word1 if any
    for p1 < len(word1) {
        output += string(word1[p1])
        p1 += 1
    }

    // Merge the remaining string from word2 if any
    for p2 < len(word2) {
        output += string(word2[p2])
        p2 += 1
    }

    return output
}