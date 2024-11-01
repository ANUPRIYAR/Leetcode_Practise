# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check_balance_height(node):
            if not node:
                return True, 0

            left_balanced, leftheight = check_balance_height(node.left)
            right_balanced, rightheight = check_balance_height(node.right)

            current_balanced = left_balanced and right_balanced and abs(leftheight - rightheight) <= 1
            current_height = max(leftheight, rightheight) + 1
            return current_balanced , current_height

        balanced, _ = check_balance_height(root)
        return balanced
            


        