/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func path(root *TreeNode, target int, sum int) int {
    if root == nil{
        return 0
    }
    
    sum += root.Val
    paths := 0
    if sum == target{
        paths += 1
    }

    paths += path(root.Left, target, sum)
    paths += path(root.Right, target, sum)

    return paths
}

func pathSum(root *TreeNode, targetSum int) int {
    if root == nil{return 0}
    
    paths:= 0

    paths += path(root, targetSum, 0)
    if root.Left!=nil{
        paths += pathSum(root.Left, targetSum)
    }

    if root.Right!=nil{
        paths += pathSum(root.Right, targetSum)
    }
    return paths
}