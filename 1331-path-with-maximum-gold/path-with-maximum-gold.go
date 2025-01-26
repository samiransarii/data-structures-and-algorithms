func getMaximumGold(grid [][]int) int {
    m := len(grid)
    n := len(grid[0])

    directions := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

    var findGold func(row, col int) int
    findGold = func(row, col int) int {
        // Base case
        if row >= m || row < 0 || col >= n || col < 0 || grid[row][col] == 0 {
            return 0
        }

        // take the gold and mark the cell as visited
        currentGold := grid[row][col]
        grid[row][col] = 0

        maxGoldFromHere := 0
        for _, direction := range directions {
            newR, newC := row+direction[0], col+direction[1]
            maxGoldFromHere = max(maxGoldFromHere, findGold(newR, newC))
        }

        // backtrack the current cell
        grid[row][col] = currentGold

        return currentGold + maxGoldFromHere
    }

    maxGold := 0
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] != 0 {
                gold := findGold(i, j)
                maxGold = max(gold, maxGold)
            }
        }
    }

    return maxGold
}