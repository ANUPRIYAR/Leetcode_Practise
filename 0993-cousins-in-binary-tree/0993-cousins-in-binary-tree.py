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
            found_x = False
            found_y = False
            for _ in range(len(queue)):
                node, depth = queue.popleft()
                print(depth)

                if node.val == x:
                    found_x = True

                if node.val == y:
                    found_y = True
                

                # if node.val == x :
                #     x_d = depth
                #     parent_x = parent[node.val]
                #     if y_flag and depth == y_d and parent_y != parent_x:
                #         x_flag = True
                #     elif not y_flag:
                #          x_flag = True
                    

                # if node.val == y :
                #     y_d = depth
                #     parent_y = parent[node.val]
                #     if x_flag and depth == x_d and parent_y != parent_x:
                #         y_flag = True
                #     elif not x_flag:
                #         y_flag = True
                if node.left and node.right:
                    if node.left.val == x and node.right.val == y or (node.left.val ==y and node.right.val == x):
                        return False

                if node.left:
                    parent[node.left.val] = node.val
                    queue.append((node.left, depth + 1))

                if node.right:
                    parent[node.right.val] = node.val
                    queue.append((node.right, depth + 1))

            if found_x and found_y:
                return True 
            if found_x or found_y:
                return False

        return False
        