class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1]* n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        # self.parent[self.find(b)] = self.find(a)
        rootA = self.find(a)
        rootB = self.find(b)
        if self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        elif self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UnionFind(4 * n * n)
        for i in range(n):
            for j in range(n):
                root = 4 * (i * n  + j)
                cell = grid[i][j]
                if cell == '/':
                    uf.union(root + 0, root + 3)
                    uf.union(root +1, root + 2)
                elif cell == '\\':
                    uf.union(root + 0, root + 1)
                    uf.union(root + 3, root + 2)
                else:
                    uf.union(root + 0, root + 1)
                    uf.union(root + 1, root + 2)
                    uf.union(root + 2, root + 3)

                if j + 1 < n:
                    uf.union(root + 1, 4*(i*n +j + 1) + 3)

                if i + 1 < n:
                    uf.union(root + 2, 4*((i + 1)* n + j) + 0)

        return sum(uf.find(x)== x for x in range(4*n*n))






        








