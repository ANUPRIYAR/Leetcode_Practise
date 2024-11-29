# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def find_balanced_height(node):
            if not node:
                return True, 0

            left_balanced, leftheight = find_balanced_height(node.left)
            right_balanced, rightheight = find_balanced_height(node.right)

            current_balanced = left_balanced and right_balanced and abs(leftheight - rightheight) <= 1
            currentheight = max(leftheight, rightheight) + 1
            return current_balanced, currentheight

        balanced, _ = find_balanced_height(root)
        return balanced


        