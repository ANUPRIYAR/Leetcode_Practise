class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        inoutdegree = defaultdict(int)
        for start, end in pairs:
            adj[start].append(end)
            inoutdegree[start] += 1
            inoutdegree[end] -= 1

        queue = deque()
        root = pairs[0][0]
        for key in inoutdegree.keys():
            if inoutdegree[key] == 1:
                root = key
                break

        path = []
        def dfs(curnode):
            while adj[curnode]:
                next_node = adj[curnode].pop()
                dfs(next_node)
                path.append((curnode, next_node))

        dfs(root)
        return path[::-1]
