# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.rslt = 0

    def height(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        lheight = 0 
        rheight = 0 

        if root.left != None:
            lheight = self.height(root.left)
        
        if root.right != None:
            rheight = self.height(root.right)

        self.rslt = max(self.rslt, lheight + rheight)

        return 1 + max(lheight, rheight)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)

        return self.rslt