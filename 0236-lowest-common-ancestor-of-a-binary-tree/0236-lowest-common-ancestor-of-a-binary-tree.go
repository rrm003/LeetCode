/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func findPath(root, target *TreeNode, path *[]*TreeNode) bool{
    if root == nil {
        return false
    }   

    *path = append(*path, root)
    if root == target {
        return true
    }

    if root.Left != nil {
        found := findPath(root.Left, target, path)
        if found {
            return true
        }
    }

    if root.Right != nil {
        found := findPath(root.Right, target, path)
        if found {
            return true
        }
    }
    
    *path = (*path)[:len(*path) - 1]

    return false
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    p_path := []*TreeNode{}
    q_path := []*TreeNode{}
    findPath(root, p, &p_path)
    findPath(root, q, &q_path)

    i := 0 
    var rslt *TreeNode
    for _, node := range p_path{
        if node.Val != q_path[i].Val {
            return rslt
        }

        rslt = node
        i += 1
    }

    return rslt
}