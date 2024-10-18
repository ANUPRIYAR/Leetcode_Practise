class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        nodes = preorder.split(',')

        if nodes[0] == '#' and len(nodes) > 1:
            return False

        length = len(nodes)
        for i in range(length):
            slots -= 1
            if slots < 0:
                return False

            if nodes[i] != '#':
                slots += 2
        return slots == 0