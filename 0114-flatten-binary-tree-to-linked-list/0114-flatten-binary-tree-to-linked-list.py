# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        stack=[]
        stack.append(root)
        rslt = None
        rslth = None
        while len(stack)>0: 
            curr = stack[len(stack)-1]
            stack = stack[:len(stack)-1]

            if curr == None:
                continue

            if rslth == None:
                rslth = curr
                rslt = rslth
            else:
                rslt.right = curr
                rslt.left = None
                rslt = rslt.right

            if curr.right !=None:
                stack.append(curr.right)
            if curr.left != None:
                stack.append(curr.left)

        root = rslth