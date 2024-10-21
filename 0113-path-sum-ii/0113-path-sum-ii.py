# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.paths = []

    def dfs(self, root, path, targetSum):
        path.append(root.val)
        if root.left == None and root.right == None:
            if sum(path) == targetSum:
                self.paths.append(path)
            
            return
        
        lpath = path.copy()
        if root.left != None:
            self.dfs(root.left, lpath, targetSum)

        rpath = path.copy()
        if root.right != None:
            self.dfs(root.right, rpath, targetSum)

        
        return

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root != None:
            self.dfs(root, [], targetSum)
            
        return self.paths