from collections import defaultdict
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        uf = {}
        n = len(source)
        def find(node):
            if node not in uf:
                uf[node] = node
            if uf[node] != node:
                uf[node] = find(uf[node])

            return uf[node]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            uf[root_x] = root_y

        for x, y in allowedSwaps:
            union(x, y)

    
        disjoint_set_counter = defaultdict(Counter)
        for i in range(n):
            # root = find(node)
            disjoint_set_counter[find(i)][source[i]] += 1

        print(disjoint_set_counter)
        res = 0
        for i in range(n):
            if disjoint_set_counter[find(i)][target[i]] > 0:
                disjoint_set_counter[find(i)][target[i]] -= 1
            else:
                res += 1

        return res







        




        