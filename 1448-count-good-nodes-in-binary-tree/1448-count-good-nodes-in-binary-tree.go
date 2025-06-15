/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func traverse(root *TreeNode, max int) []int {
    rslt := []int{}
    if root == nil {
        return rslt
    }

    if root.Val >= max {
        rslt = append(rslt, root.Val)
        max = root.Val
    }

    if root.Left != nil {
        rslt = append(rslt, traverse(root.Left, max)...)
    }

    if root.Right != nil {
        rslt = append(rslt, traverse(root.Right, max)...)
    }

    return rslt
}

func goodNodes(root *TreeNode) int {
    goodNodes := traverse(root, -math.MaxInt)
    fmt.Println(goodNodes)
    return len(goodNodes)
}