# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = []
        def dfs(node, left= False):
            if not node:
                return 
            
            if not node.left and not node.right and left:
                total.append(node.val)

            dfs(node.left, left=True)
            dfs(node.right, left=False)
           
        dfs(root)
        return sum(total)





            
            

            



        