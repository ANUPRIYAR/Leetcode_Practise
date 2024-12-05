"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)

        answer = []
        while queue:
            nodes = []
            for i in range(len(queue)):
                node = queue.popleft()
                nodes.append(node.val)

                for child in node.children:
                    queue.append(child)

            answer.append(nodes[:])

        return answer


        


        