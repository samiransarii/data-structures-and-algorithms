func findDiagonalOrder(mat [][]int) []int {
    if mat == nil || len(mat) == 0 {
        return []int{0}
    }
    
    m := len(mat)
    n := len(mat[0])
    output := []int{}
    diagonals := map[int][]int{}

    // Store the diagonal elements in the map
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            diagonals[i+j] = append(diagonals[i+j], mat[i][j])
        }
    }

    keys := make([]int, 0, len(diagonals))
    for key := range diagonals {
        keys = append(keys, key)
    }
    // Sort the keys
    sort.Ints(keys)

    // Store the diagonal element in the output
    flip := true
    for _, key:= range keys {
        values := diagonals[key]
        if flip {
            reverseValues := reverse(values)
            output = append(output, reverseValues...)

        } else {
            output = append(output, values...)
        }
        
        // Toggle flip
        flip = !flip
    }

    return output
}

func reverse(slice []int) []int {
    left, right := 0, len(slice)-1
    for left < right {
        slice[left], slice[right] = slice[right], slice[left]
        left++
        right--
    }

    return slice
}