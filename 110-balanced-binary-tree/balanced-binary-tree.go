/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isBalanced(root *TreeNode) bool {
    isBalanced := true

    var dfs func(node *TreeNode) int
    dfs = func(node *TreeNode) int {
        // Base case
        if node == nil {
            return 0
        }

        left := 1 + dfs(node.Left)
        right := 1 + dfs(node.Right)

        // If height difference is greater tha 1
        // set isBalanced to false
        if math.Abs(float64(left) - float64(right)) > 1 {
            isBalanced = false
        }

        return max(left, right)
    }
    
    dfs(root)
    return isBalanced    
}