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
    level int
}

func rightSideView(root *TreeNode) []int {
    if root == nil {
        return []int{}
    }
    
    queue := []*NodeInfo{{root, 0}}
    lookup := make(map[int][]*TreeNode)

    for len(queue) > 0 {
        curr := queue[0]
        if _, ok := lookup[curr.level]; !ok {
            lookup[curr.level] = []*TreeNode{}
        }

        lookup[curr.level] = append(lookup[curr.level], curr.Node)

        queue = queue[1:]

        if curr.Node.Left != nil {
            queue = append(queue, &NodeInfo{curr.Node.Left, curr.level + 1})
        }

        if curr.Node.Right != nil {
            queue = append(queue, &NodeInfo{curr.Node.Right, curr.level + 1})
        }
    }

    rslt := make([]int, 0)
    l := len(lookup)
    i:=0 
    for i < l {
        v := lookup[i]
        rslt = append(rslt, v[len(v)-1].Val)
        i++
    }

    return rslt
}