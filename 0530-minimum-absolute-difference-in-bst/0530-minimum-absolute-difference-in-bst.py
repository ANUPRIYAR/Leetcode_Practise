# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        queue = deque()
        queue.append(root)
        values = []

        while queue:
            node = queue.popleft()

            for val in values:
                min_diff = min(min_diff, abs(node.val - val))

            values.append(node.val)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
       
        return min_diff


        