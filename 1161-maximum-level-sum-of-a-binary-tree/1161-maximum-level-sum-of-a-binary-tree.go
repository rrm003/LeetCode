/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type NodeInfo struct {
    Node *TreeNode
    Level int
}

func maxLevelSum(root *TreeNode) int {
    queue := []*NodeInfo{{root, 0}}
    lookup := make(map[int][]*TreeNode) 

    for len(queue) > 0 {
        curr := queue[0]
        queue = queue[1:]

        if _, ok := lookup[curr.Level]; !ok {
            lookup[curr.Level] = []*TreeNode{}
        }

        lookup[curr.Level] = append(lookup[curr.Level], curr.Node)

        if curr.Node.Left != nil {
            queue = append(queue, &NodeInfo{curr.Node.Left, curr.Level + 1})
        }

        if curr.Node.Right != nil {
            queue = append(queue, &NodeInfo{curr.Node.Right, curr.Level + 1})
        }
    }

    i := 0 
    l := len(lookup)
    max_sum := 0
    max_level := 0

    for i < l {
        nodes := lookup[i]
        total := 0 
        for _, node := range nodes{
            total += node.Val
        }

        if total > max_sum {
            max_sum = total 
            max_level = i
        }

        i++
    }

    return max_level + 1
}