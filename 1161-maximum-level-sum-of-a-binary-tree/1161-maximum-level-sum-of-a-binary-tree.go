/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func sum(arr []int) int{
    sum := 0
    for _, a := range arr{
        sum += a
    }

    return sum
}

func levelOrder(root *TreeNode, level int, order map[int][]int) {
    if root == nil {
        return
    }

    if _, ok := order[level]; !ok{
        order[level] = []int{}
    }

    order[level] = append(order[level], root.Val)

    levelOrder(root.Left, level + 1, order)
    levelOrder(root.Right, level + 1, order)
}

func maxLevelSum(root *TreeNode) int {
    order := make(map[int][]int)
    levelOrder(root, 1, order)

    global := 0
    level := -1
    for k, val := range order{
        local := sum(val)

        if local > global{
            level = k
            global = max(local, global)
        }
    }

    return level
}