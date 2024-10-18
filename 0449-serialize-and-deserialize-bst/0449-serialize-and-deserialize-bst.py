# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        sb = []
        self.serializehelper(root, sb)
        return ''.join(sb)


    def serializehelper(self, root, sb):
        if root is None:
            sb.append('#,')
            return

        sb.append(str(root.val) + ',')
        self.serializehelper(root.left, sb)
        self.serializehelper(root.right, sb)

        

    def deserialize(self, nodes: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        nodes = nodes.split(',')
        nodes.pop()  # popping last comma
        return self.deserializehelper(iter(nodes))


    def deserializehelper(self, nodes):
        value = next(nodes)
        if value == '#':
            return None
        root = TreeNode(int(value))
        root.left = self.deserializehelper(nodes)
        root.right = self.deserializehelper(nodes)
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans