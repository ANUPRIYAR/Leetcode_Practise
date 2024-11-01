# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(root, currsum):
            if not root:
                return False

            currsum += root.val
            if not root.left and not root.right: # to confirm is its a leaf node
                if currsum == targetSum:
                    return True
                # else:
                #     # currsum -= root.val
                #     return False
            return dfs(root.left, currsum) or dfs(root.right, currsum)

        return dfs(root, 0)


            



            
        