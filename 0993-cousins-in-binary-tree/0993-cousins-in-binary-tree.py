# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque()
        queue.append(root)
        # x_d = -1
        # y_d = -1
        # parent = defaultdict(int)
        # parent[root.val] = -1

        while queue:
            found_x = False
            found_y = False
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.val == x:
                    found_x = True

                if node.val == y:
                    found_y = True
                

                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or (node.left.val ==y and node.right.val == x):
                        return False

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if found_x and found_y:
                return True 
            if found_x or found_y:
                return False

        return False
        