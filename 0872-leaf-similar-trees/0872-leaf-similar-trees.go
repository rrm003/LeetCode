/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func getLeaves(root *TreeNode)  []int{
    rslt := []int{}
    if root == nil {
        return rslt
    }

    if root.Left == nil && root.Right == nil {
        rslt = append(rslt, root.Val)
    }

    if root.Left != nil {
        left := getLeaves(root.Left)
        rslt = append(rslt, left...)
    }

    if root.Right != nil {
        right := getLeaves(root.Right)
        rslt = append(rslt, right...)
    }


    return rslt
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
    leaves1 := getLeaves(root1)
    leaves2 := getLeaves(root2)

    if len(leaves1) != len(leaves2) {
        return false
    }


    for i := 0; i < len(leaves1); i ++ {
        if leaves1[i] != leaves2[i] {
            return false
        }
    }

    return true
}