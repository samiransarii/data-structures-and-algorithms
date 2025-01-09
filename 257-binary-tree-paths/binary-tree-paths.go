/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func binaryTreePaths(root *TreeNode) []string {
    var output []string

    if root == nil {
        return output
    }

    var dfs func(currNode *TreeNode, path string) 
    dfs = func(currNode *TreeNode, path string) {
        // return if currNode is nill
        if currNode == nil {
            return
        }

        // If leaf node append the path to the output
        // and return
        if (currNode.Left == nil && currNode.Right == nil) {
            path += strconv.Itoa(currNode.Val)
            output = append(output, path)
            return
        }

        path += fmt.Sprintf("%d->", currNode.Val)

        dfs(currNode.Left, path) // Go Left
        dfs(currNode.Right, path) // Go Right
    }


    dfs(root, "")
    return output
}