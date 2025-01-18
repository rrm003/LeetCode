# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rslt = []
        if root == None:
            return []

        if root.left != None:
            lrslt = self.postorderTraversal(root.left)
            rslt.extend(lrslt)
        
        if root.right != None:
            rrslt = self.postorderTraversal(root.right)
            rslt.extend(rrslt)
        
        rslt.append(root.val)

        return rslt