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

        if not root.left and not root.right:
            return root.val

        queue = deque()
        queue.append(root)

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    prev_node = node
                
                if node.right:
                    queue.append(node.right)
                    if not node.left:
                        prev_node = node

        if prev_node.left:
            return prev_node.left.val
        elif prev_node.right:
            return prev_node.right.val

        return prev_node.val

        


        