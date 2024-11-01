# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def finddepth(node):
            if not node.left and not node.right:
                return  1        

            left = finddepth(node.left) if node.left else float('inf')
            right = finddepth(node.right) if node.right else float('inf')

            return 1 + min(left, right)

        return finddepth(root)
            