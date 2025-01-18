# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # iterative approach
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        rslt = []
        if root == None:
            return rslt

        stack.append(root)
        
        while len(stack) > 0:
            curr = stack[-1]
            rslt.append(curr.val)

            stack = stack[:-1]

            if curr.right != None:
                stack.append(curr.right)

            if curr.left != None:
                stack.append(curr.left)
        
        return rslt