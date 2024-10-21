# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, pathSum, targetSum):
        pathSum += root.val
        
        if root.left == None and root.right == None:
            print("pathSum", pathSum, "targetSum", targetSum)
            return pathSum == targetSum
        

        rslt = False
        if root.left != None:
            rslt = rslt or self.dfs(root.left, pathSum, targetSum)
        
        if root.right != None:
            rslt = rslt or self.dfs(root.right, pathSum, targetSum)        

        return rslt


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False

        return self.dfs(root, 0, targetSum)