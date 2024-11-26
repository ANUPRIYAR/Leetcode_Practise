class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        indegree = [0]*n
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        strongest = []
        for i in range(n):
            if indegree[i] == 0:
                strongest.append(i)

        if len(strongest) > 1 or  len(strongest) == 0 :
            return -1 

        return strongest[0]





        