/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode, level int, order map[int][]int){
    if root == nil{
        return 
    }

    if _, ok := order[level]; !ok{
        order[level] = []int{}
    }

    order[level] = append(order[level], root.Val)

    levelOrder(root.Left, level + 1, order)
    levelOrder(root.Right, level + 1, order)

    return
}

func rightSideView(root *TreeNode) []int {
    order := make(map[int][]int)

    levelOrder(root, 0, order)

    l := len(order)
    rslt := []int{}
    for i:=0; i<l; i++{
        rslt = append(rslt, order[i][len(order[i])-1])
    }

    return rslt
}