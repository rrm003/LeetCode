# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.start_path = ""
        self.dest_path = ""

    def dfs_start_element(self, root, startValue, destValue, path):
        if root == None:
            return

        stack = [(root, "")]
        
        while len(stack) > 0 : 
            curr, path = stack.pop()
            if curr.val == startValue:
                self.start_path = path
            
            if curr.val == destValue:
                self.dest_path = path

            if self.start_path != "" and self.dest_path != "":
                return 

            if curr.left != None:
                stack.append((curr.left, path + "L"))
            
            if curr.right != None:
                stack.append((curr.right, path + "R"))
        


    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.dfs_start_element(root, startValue, destValue, "")

        common = 0
        while common < len(self.start_path) and common < len(self.dest_path):
            if self.start_path[common] != self.dest_path[common]:
                break
            
            common += 1
        
        start_path = self.start_path[common:]
        dest_path = self.dest_path[common:]
        
        rslt = "U" * len(start_path)
        rslt += dest_path

        return rslt