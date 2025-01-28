func permute(nums []int) [][]int {
    var current []int
    var result [][]int
    visited := make(map[int]bool)



    var findPermutation func()
    findPermutation = func() {
        if len(current) == len(nums) {
            // Make a copy of the current permutation
            permutation := make([]int, len(current))
            copy(permutation, current)
            result = append(result, permutation)
            return
        }

        // Iterate through the nums array
        for _, num := range nums {
            if !visited[num] {
                current = append(current, num)
                visited[num] = true

                // Recurse to build the next level of permutation
                findPermutation()

                // Backtrack
                current = current[:len(current) - 1]
                visited[num] = false
            }
        }
    }

    findPermutation()
    return result
}