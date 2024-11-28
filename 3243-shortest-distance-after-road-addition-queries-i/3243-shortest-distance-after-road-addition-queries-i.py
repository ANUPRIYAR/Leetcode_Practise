class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Build Graph
        adj = defaultdict(list)
        for i in range(n-1):
            adj[i].append(i + 1)


        def bfs(node):
            queue = deque()
            visited = set()

            queue.append((node, 0))
            visited.add(node)

            while queue:
                node, dist = queue.popleft()

                if node == n-1:
                    return dist

                for child in adj[node]:
                    if child not in visited:
                        visited.add(child)
                        queue.append((child, dist + 1))

            return -1 

        answer = []
        for u, v in queries:
            adj[u].append(v)
            answer.append(bfs(0))


        return answer




    
        