/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func searchBST(root *TreeNode, val int) *TreeNode {
    if root == nil {
        return nil
    }

    if root.Val == val{
        fmt.Println(root, root.Val)
        return root
    }

    var rslt *TreeNode
    if root.Val > val {
        rslt = searchBST(root.Left, val)
    }else{
        rslt = searchBST(root.Right, val)
    }

    return rslt
}