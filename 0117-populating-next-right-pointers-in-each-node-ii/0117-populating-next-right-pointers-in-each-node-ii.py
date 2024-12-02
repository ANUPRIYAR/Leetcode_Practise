"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        queue = deque()
        queue.append(root)

        while queue:
            LevelSize = len(queue)
            for i in range(LevelSize):
                currentnode = queue.popleft()
                
                if i < LevelSize -1:
                    currentnode.next = queue[0]

                if currentnode.left:
                    queue.append(currentnode.left)
                
                if currentnode.right:
                    queue.append(currentnode.right)

        return root

        