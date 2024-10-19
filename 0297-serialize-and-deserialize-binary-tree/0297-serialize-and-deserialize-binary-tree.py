# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return self.shelper(root)
        
        
    def shelper(self, node):
        if node is None:
            return 'X,'

        left_serialized = self.shelper(node.left)
        right_serialized = self.shelper(node.right)
        return str(node.val) + "," + left_serialized +  right_serialized


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(',')
        return self.deserializehelper(iter(nodes))
               

    def deserializehelper(self, nodes):
        value = next(nodes)
        if value == 'X':
            return None

        root = TreeNode(int(value))
        root.left = self.deserializehelper(nodes)
        root.right = self.deserializehelper(nodes)
        return root
        

        



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))