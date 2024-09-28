# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        
        rslt = []
        
        rslt.extend(self.inorderTraversal(root.left))
        rslt.append(root.val)
        rslt.extend(self.inorderTraversal(root.right))

        return rslt
        