# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        nodesum = 0

        answer = []
        while queue:
            nodesum = 0
            total_nodes = len(queue)
            for _ in range(len(queue)):
                node = queue.popleft()

                nodesum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            answer.append(nodesum/total_nodes)


        return answer




        