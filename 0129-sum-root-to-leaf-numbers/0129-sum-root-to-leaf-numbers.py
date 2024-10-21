# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.totalSum = 0

    def dfs(self, root, path):
        path = path * 10 + root.val

        if root.left == None and root.right == None:
            self.totalSum += path
            return
        
        if root.left != None:
            self.dfs(root.left, path)
        
        if root.right != None:
            self.dfs(root.right, path)
        
        return


    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root!=None:
            self.dfs(root, 0)
        
        return self.totalSum