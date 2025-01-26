func getLastMoment(n int, left []int, right []int) int {
    
    output := 0
    // For ants going left, total distance to cover is left[i]
    for _, num := range left {
        output = max(output, num)
    }

    // For ants going right, total distance to cover before falling is lengthOfPlank - right[i]
    for _, num := range right {
        output = max(output, n - num)
    }

    return output
}