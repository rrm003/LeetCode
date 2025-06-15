/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
    if root == nil {
        return 0
    }

    height := 1

    if root.Left != nil {
        h := 1 + maxDepth(root.Left)
        if h > height {
            height = h
        }
    }
    
    if root.Right != nil {
        h := 1 + maxDepth(root.Right)
        if h > height {
            height = h
        }
    }

    return height
}