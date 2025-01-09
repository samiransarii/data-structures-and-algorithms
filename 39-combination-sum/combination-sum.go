func combinationSum(candidates []int, target int) [][]int {
	var output [][]int
	N := len(candidates)

	var findCombination func(idx int, currPath []int, currTotal int)
	findCombination = func(idx int, currPath []int, currTotal int) {
		if currTotal == target {
			copyPath := make([]int, len(currPath))
			copy(copyPath, currPath)
			output = append(output, copyPath)
			return
		}

		if idx >= N || currTotal > target {
			return
		}

		// Take the current element
		currElement := candidates[idx]
		currPath = append(currPath, currElement)
		findCombination(idx, currPath, currTotal+currElement)

		// Skip the current element -- backtrack
		currPath = currPath[:len(currPath)-1]
		findCombination(idx+1, currPath, currTotal)
	}

	findCombination(0, []int{}, 0)

	return output
}