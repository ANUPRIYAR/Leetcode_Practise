# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()

        left = True
        queue.append(root)
        ans = []
        while queue:
            level = []
            left  = not left

            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if left:
                    if node.left:
                        queue.append(node.left )
                    if node.right:
                        queue.append(node.right)
                else:
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
            
            
            ans.append(level)

        return ans
        