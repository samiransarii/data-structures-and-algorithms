func longestCommonSubsequence(text1 string, text2 string) int {
    N1 := len(text1)
    N2 := len(text2)
    
    var dp = make([][]int, N1)
    for i := range dp {
        dp[i] = make([]int, N2)
        for j := range dp[i] {
            dp[i][j] = -1
        }
    }

    // Define the recursive function to find LCS
    var findLCS func(p1 int, p2 int) int
    findLCS = func(p1 int, p2 int) int {
        // Return 0 if indx is out of bound
        // for any of the string
        if p1 >= N1 || p2 >= N2 {
            return 0
        }

        if dp[p1][p2] != -1 {
            return dp[p1][p2]
        }

        // If current Indx matches for both the strings
        // add 1 and explore other indxs
        if text1[p1] == text2[p2] {
            dp[p1][p2] = 1 + findLCS(p1 + 1, p2 + 1)
            return dp[p1][p2]
        } else {
            // Else explore both the possiblities of skipping one
            // Idx from both string one by one and return the max
            // answer.
            dp[p1][p2] = max(findLCS(p1 + 1, p2), findLCS(p1, p2 + 1))
            return dp[p1][p2]
        }
    }

    output := findLCS(0, 0)
    return output
}