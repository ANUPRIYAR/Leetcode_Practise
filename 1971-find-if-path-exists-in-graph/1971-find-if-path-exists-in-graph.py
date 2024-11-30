class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(source, dest):
            queue = deque()
            visited = set()

            queue.append(source)
            visited.add(source)

            while queue:
                node = queue.popleft()

                if node == dest:
                    return True

                for child in graph[node]:
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)


            return False

        return bfs(source, destination)



        