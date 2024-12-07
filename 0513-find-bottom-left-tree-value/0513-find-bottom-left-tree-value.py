# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        queue = deque()
        queue.append(root)

        while queue:
            levelsize = len(queue)
            for i in range(levelsize):
                node = queue.popleft()
                if i == 0:
                    leftmostnode = node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

        return leftmostnode

        