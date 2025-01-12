func countSubstrings(s string) int {
    N := len(s)

    // Check if palindromic string
    var isPalindrome func(i int, j int) bool
    isPalindrome = func(i int, j int) bool {
        if i > j {
            return true
        }
        
        if s[i] == s[j] {
            return isPalindrome(i+1, j-1)
        }

        return false
    }

    // Find all the substrings -> bruteforce
    count := 0
    for i := 0; i < N; i++ {
        for j := i; j < N; j++ {
            if isPalindrome(i, j) {
                count ++
            }
        }
    } 

   return count
}