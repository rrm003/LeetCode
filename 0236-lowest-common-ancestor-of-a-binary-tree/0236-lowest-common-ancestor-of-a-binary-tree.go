/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func dfs(root *TreeNode, target *TreeNode) ([]*TreeNode, bool){
    if root == nil {return []*TreeNode{}, false}
    if root == target{
        return []*TreeNode{root}, true
    }

    rslt := []*TreeNode{root}
    path, found := dfs(root.Left, target)
    if found{
        rslt = append(rslt, path...)
        return rslt, true
    }

    path, found = dfs(root.Right, target)
    if found{
        rslt = append(rslt, path...)
        return rslt, true
    }

    return rslt, false
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    if root == nil {return nil}
    path1, _ := dfs(root, p)
    path2, _ := dfs(root, q)

    l := min(len(path1), len(path2))

    var rslt *TreeNode
    for i:=0; i < l; i++{
        if path1[i] == path2[i] {
            rslt = path1[i]
        }else{
            break
        }
    }

    return rslt
}