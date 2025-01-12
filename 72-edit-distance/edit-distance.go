func minDistance(word1 string, word2 string) int {
    M := len(word1) 
    N := len(word2)

    // Initialize dp array
    var dp = make([][]int, M)
    for i := range dp {
        dp[i] = make([]int, N)
        for j := range dp[i] {
            dp[i][j] = -1
        }
    }

    var findMinDistance func(i int, j int) int
    findMinDistance = func(i int, j int) int {
        // Base case := word1 if finished insert the remaining characters from word2
        if i >= M {
            return N - j
        // Base case2 := word2 if finished delete the remaining characters from word1
        } else if j >= N {
            return M - i
        }

        if dp[i][j] != -1 {
            return dp[i][j]
        }

        // If charcters matched solve for the next characters
        if word1[i] == word2[j] {
            dp[i][j] = findMinDistance(i + 1, j + 1)
            return dp[i][j]
        
        // If characters differes, explore all the possibilities of
        // Inserting, deleting, and replacing
        } else {
            insert := 1 + findMinDistance(i, j + 1)
            delete := 1 + findMinDistance(i + 1, j)
            replace := 1 + findMinDistance(i + 1, j + 1)

            dp[i][j] = min(insert, delete, replace)
            return dp[i][j]
        }
    }

    output := findMinDistance(0, 0)
    return output
}