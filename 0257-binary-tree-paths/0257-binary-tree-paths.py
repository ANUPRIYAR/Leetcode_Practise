# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def dfs(node, cur_path):
            if not node:
                return 

            cur_path += str(node.val)

            if not node.left and not node.right: # check if leaf node, then update result
                paths.append(cur_path)
            else:
                cur_path += "->"
                dfs(node.left, cur_path) # else just do dfs
                dfs(node.right, cur_path) # since we are already appending node.val

        dfs(root, "")
        return paths

      