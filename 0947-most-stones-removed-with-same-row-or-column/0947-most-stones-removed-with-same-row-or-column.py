class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = {}
        def find(node):
            if node not in uf:
                uf[node] = node
            if uf[node] != node:
                uf[node] = find(uf[node])

            return uf[node]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            uf[root_u] = root_v

        stone_nodes = []
        max_row = 0
        max_col = 0

        for x, y in stones:
            max_row =  max(max_row, x)
            max_col = max(max_col, y)

        # stone_nodes = []
        for x, y in stones:
            # stone_nodes.append([x, y + max_row + 1])
            union(x, y + max_row + 1)

        num_connected = 0
        for node in uf:
            if find(node) == node:
                num_connected += 1

        return len(stones) - num_connected
        




        