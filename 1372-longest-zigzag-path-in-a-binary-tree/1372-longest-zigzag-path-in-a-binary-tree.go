/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func dfs(root *TreeNode, dir string, path int) int{
    if root == nil {
        return path - 1
    }

    rslt := 0
    if dir == "R" {
        rslt = dfs(root.Left, "L", path + 1)
        rslt = max(rslt, dfs(root.Right, "R", 1))
    }

    if dir == "L" {
        rslt = dfs(root.Right, "R", path + 1)
        rslt = max(rslt, dfs(root.Left, "L", 1))
    }

    return rslt
}

func longestZigZag(root *TreeNode) int {
    if root == nil{
        return 0
    }

    left := dfs(root.Left, "L", 1) 
    right := dfs(root.Right, "R", 1)

    return max(left, right)
}