/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isBalanced(root *TreeNode) bool {
    output := true

    var dfs func(node *TreeNode) int
    dfs = func(node *TreeNode) int {
        // Base case
        if node == nil {
            return 0
        }

        left := 1 + dfs(node.Left)
        right := 1 + dfs(node.Right)

        if math.Abs(float64(left) - float64(right)) > 1 {
            output = false
        }

        return max(left, right)
    }
    
    dfs(root)
    return output    
}