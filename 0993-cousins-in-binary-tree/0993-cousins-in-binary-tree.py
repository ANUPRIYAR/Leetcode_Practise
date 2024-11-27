# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque()
        queue.append((root, 0))
        x_d = -1
        y_d = -1
        parent = defaultdict(int)
        parent[root.val] = -1

        while queue:
            x_flag = False
            y_flag = False
            for _ in range(len(queue)):
                node, depth = queue.popleft()
                print(depth)

                if node.val == x :
                    x_d = depth
                    parent_x = parent[node.val]
                    if y_flag and depth == y_d and parent_y != parent_x:
                        x_flag = True
                    elif not y_flag:
                         x_flag = True

                    

                if node.val == y :
                    y_d = depth
                    parent_y = parent[node.val]
                    if x_flag and depth == x_d and parent_y != parent_x:
                        y_flag = True
                    elif not x_flag:
                        y_flag = True

                if node.left:
                    parent[node.left.val] = node.val
                    queue.append((node.left, depth + 1))

                if node.right:
                    parent[node.right.val] = node.val
                    queue.append((node.right, depth + 1))

            if x_flag and y_flag:
                return True 
            if x_flag or y_flag:
                return False

        return False
        