/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pathSum(root *TreeNode, targetSum int) int {
    var output int

    var dfs func(node *TreeNode, currTotal int)
    dfs = func(node *TreeNode, currTotal int) {
        // Base Case
        if node == nil {
            return
        }

        currTotal += node.Val
        if currTotal == targetSum {
            output += 1
        }

        // Recursion
        dfs(node.Left, currTotal)
        dfs(node.Right, currTotal)
    }


    var runDFSFromEveryNode func(node *TreeNode)
    runDFSFromEveryNode = func(node *TreeNode) {
        if node == nil {
            return
        }

        dfs(node, 0)

        runDFSFromEveryNode(node.Left)
        runDFSFromEveryNode(node.Right)
    }

    runDFSFromEveryNode(root)
    return output
}