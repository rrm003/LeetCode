# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root==None: return 0

        total = 0
        queue = []
        queue.append(root)
        
        while len(queue) > 0:
            curr = queue[0]
            queue = queue[1:]

            if curr.val >= low and curr.val <= high:
                total += curr.val
            
            if curr.left != None:
                queue.append(curr.left)
            
            if curr.right != None:
                queue.append(curr.right)
        
        return total