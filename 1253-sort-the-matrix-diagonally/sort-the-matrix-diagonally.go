func diagonalSort(mat [][]int) [][]int {
    m := len(mat)
    n := len(mat[0])
    diagonals := map[int][]int{}

    // Get the diagonal elements in a map    
    for row := 0; row < m; row++ {
        for col := 0; col < n; col++ {
            diagonals[row-col] = append(diagonals[row-col], mat[row][col])
        }
    } 

    // Sort the diagonals element stored in the map
    for _, values := range diagonals {
        sort.Slice(values, func(i, j int) bool {
            return values[i] < values[j]
        })
    }

    // Replace back the diagonal elements back in the matrix
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            mat[i][j] = diagonals[i-j][0]
            diagonals[i-j] = diagonals[i-j][1:]
        }
    }  

    return mat
}