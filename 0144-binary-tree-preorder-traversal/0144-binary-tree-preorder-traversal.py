# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rslt = []

        if root == None:
            return []

        print(root.val)
        rslt.append(root.val)

        if root.left != None:
            lrslt = self.preorderTraversal(root.left)
            rslt.extend(lrslt)

        if root.right != None:
            rrslt = self.preorderTraversal(root.right)
            rslt.extend(rrslt)

        return rslt