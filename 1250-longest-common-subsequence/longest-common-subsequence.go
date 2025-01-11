func longestCommonSubsequence(text1 string, text2 string) int {
    M := len(text1) + 1
    N := len(text2) + 1

    var dp = make([][]int, M)
    for i := range dp {
        dp[i] = make([]int, N)
    }

    for i := 1; i < M; i++ {
        for j := 1; j < N; j++ {
            if text1[i-1] == text2[j-1] {
                dp[i][j] = 1 + dp[i-1][j-1]
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            }
        }
    }

    return dp[M - 1][N - 1]
}