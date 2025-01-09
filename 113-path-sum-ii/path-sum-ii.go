/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pathSum(root *TreeNode, targetSum int) [][]int {
    var output [][]int

    var dfs func(node *TreeNode, currPath []int, currTotal int)
    dfs = func(node *TreeNode, currPath []int, currTotal int) {
        // Base Case
        if node == nil {
            return
        }

        currTotal += node.Val
        currPath = append(currPath, node.Val)

        if (node.Left == nil && node.Right == nil && currTotal == targetSum) {
            copyPath := make([]int, len(currPath))    
            copy(copyPath, currPath)
            output = append(output, copyPath)
        }

        // Recursion
        dfs(node.Left, currPath, currTotal)
        dfs(node.Right, currPath, currTotal)
    }

    dfs(root, []int{}, 0)
    return output
}