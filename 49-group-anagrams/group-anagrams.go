func groupAnagrams(strs []string) [][]string {
    var groups = make(map[string][]string)
    var output = [][]string{}

    for _, word := range strs {
        runes := []rune(word)
        sort.Slice(runes, func(i, j int) bool {
            return runes[i] < runes[j]
        })
        
        key := string(runes)
        groups[key] = append(groups[key], word)
    }

    for _, v := range groups {
        output = append(output, v)
    }

    return output
}