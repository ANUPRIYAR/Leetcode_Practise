# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check_balance(node):
            if not node:
                return True, 0

            left_balanced, leftheight = check_balance(node.left)
            right_balanced, rightheight = check_balance(node.right)

            cur_balanced = (left_balanced and right_balanced) and abs(leftheight- rightheight) <= 1

            return cur_balanced, max(leftheight, rightheight) + 1


        balanced, _ = check_balance(root)
        return balanced
        