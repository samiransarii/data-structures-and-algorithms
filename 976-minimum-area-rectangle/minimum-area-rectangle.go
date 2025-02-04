func minAreaRect(points [][]int) int {
    n := len(points) 
    pointMap := make(map[[2]int]bool)

    for _, p := range points {
        pointMap[[2]int{p[0], p[1]}] = true
    }

    minArea := math.MaxInt32
    found := false

    // Iterate over all pairs of points
    for i := 0; i < n; i++ {
        for j := i+1; j < n; j++ {
            x1, y1 := points[i][0], points[i][1]
            x2, y2 := points[j][0], points[j][1]

            // Check if two points are diagonal or not
            if x1 != x2 && y1 != y2 {
                // Check if the diagonal points are in the map or not
                if pointMap[[2]int{x1, y2}] && pointMap[[2]int{x2, y1}] {
                    area := abs(x2-x1) * abs(y2-y1)
                    if area < minArea {
                        minArea = area
                        found = true
                    }
                }
            }
        }
    }

    if found {
        return minArea
    }

    return 0
}

func abs(x int) int {
    if x < 0 {
        return -x
    }

    return x
}