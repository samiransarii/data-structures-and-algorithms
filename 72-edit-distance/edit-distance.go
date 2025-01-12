func minDistance(word1 string, word2 string) int {
    M := len(word1) 
    N := len(word2)

    // Initialize dp array
    var dp = make([][]int, M+1)
    for i := range dp {
        dp[i] = make([]int, N+1)
    }

    for i := 0; i <= M; i ++ {
        for j := 0; j <= N; j++ {
            if i == 0 || j == 0 {
                dp[i][j] = i+j

            } else if word1[i-1] == word2[j-1] {
                dp[i][j] = dp[i-1][j-1]

            } else {
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
            }
        }
    } 

    return dp[M][N]
}