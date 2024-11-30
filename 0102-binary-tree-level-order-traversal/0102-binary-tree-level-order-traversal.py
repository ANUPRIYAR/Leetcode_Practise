# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        nodes_by_level = []

        def bfs(node):
            queue = deque()
            visited = set()

            queue.append(node)
            visited.add(node)

            while queue:
                cur_level = []

                for i in range(len(queue)):
                    node = queue.popleft()

                    cur_level.append(node.val)

                    if node.left:
                        queue.append(node.left)
                   
                    if node.right:
                         queue.append(node.right)

                nodes_by_level.append(cur_level)

        bfs(root)
        return nodes_by_level




        