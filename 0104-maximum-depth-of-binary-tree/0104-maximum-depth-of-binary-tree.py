# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxdepth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, depth):
            if not node:
                return

            # depth += 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

            self.maxdepth = max(self.maxdepth, depth)

        dfs(root, 1)

        return self.maxdepth



        