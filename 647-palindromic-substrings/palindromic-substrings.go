func countSubstrings(s string) int {
    N := len(s)

    dp := make([][]int, N+1)
    for i := range dp {
        dp[i] = make([]int, N+1)
            for j := range dp[i] {
                dp[i][j] = -1
            }
    }

    // Check if palindromic string
    var isPalindrome func(i int, j int) int
    isPalindrome = func(i int, j int) int {
        if i > j {
            return 1
        }

        if dp[i][j] != -1 {
            return dp[i][j]
        }
        
        if s[i] == s[j] {
            dp[i][j] = isPalindrome(i+1, j-1)
            return dp[i][j]
        }

        return 0
    }

    // Find all the substrings -> bruteforce
    count := 0
    for i := 0; i < N; i++ {
        for j := i; j < N; j++ {
            if isPalindrome(i, j) == 1 {
                count ++
            }
        }
    } 
    
    return count
}