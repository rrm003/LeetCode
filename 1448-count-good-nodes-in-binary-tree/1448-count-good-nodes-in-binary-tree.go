/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func traverse(root *TreeNode, stack []int) int{
    if root == nil {return 0}

    count := 0
    if len(stack) == 0 || root.Val >= stack[len(stack)-1]{
        stack = append(stack, root.Val)
        count += 1
    }

    count += traverse(root.Left, stack)
    count += traverse(root.Right, stack)

    stack = stack[:len(stack)-1]

    return count
}

func goodNodes(root *TreeNode) int {
    return traverse(root, []int{})   
}