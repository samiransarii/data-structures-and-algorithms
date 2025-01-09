/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
    var dfs func(node *TreeNode) int
    dfs = func(node *TreeNode) int {
        // Base case
        if node == nil {
            return 0
        }

        left := 1 + dfs(node.Left)
        right := 1 + dfs(node.Right)

        return max(left, right)
    }
    
    depth := dfs(root)
    return depth
}