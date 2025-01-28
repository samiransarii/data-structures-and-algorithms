func rotate(matrix [][]int)  {
    n := len(matrix)
    
    // Calculate the transpose of matrix
    for i := 0; i < n; i++ {
        for j := i; j < n; j++ {
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        }
    }

    // Reverse each row
    for i := 0; i < n; i++ {
        reverse(matrix[i])
    }
}

func reverse(slice []int) {
    left, right := 0, len(slice)-1
    for left < right {
        slice[left], slice[right] = slice[right], slice[left]
        left++
        right--
    }
}