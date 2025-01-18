# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rslt = []
        if root == None:
            return []

        if root.left != None:
            lrslt = self.inorderTraversal(root.left)
            rslt.extend(lrslt)

        rslt.append(root.val)

        if root.right != None:
            rrslt = self.inorderTraversal(root.right)
            rslt.extend(rrslt)
        
        return rslt