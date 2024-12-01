"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.clone = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        if node in self.clone:
            return self.clone[node]

        cloneTree = Node(node.val, [])

        self.clone[node] = cloneTree
        for ngbr in node.neighbors:
            cloneTree.neighbors.append(self.cloneGraph(ngbr))

        return cloneTree
        


        