class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        inOutDeg = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            inOutDeg[start] += 1
            inOutDeg[end] -= 1


        # finding the start node
        root = pairs[0][0]
        for node in inOutDeg:
            if inOutDeg[node] == 1:
                root = node
                break


        path = []
        def dfs(curr):
            while graph[curr]:
                next_node = graph[curr].pop()
                dfs(next_node)
                path.append((curr, next_node))

        dfs(root)
        return path[::-1]


