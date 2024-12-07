class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, (u, v) in enumerate(equations):
            adj[u].append((v, values[i]))
            adj[v].append((u, 1/values[i]))
        

        def bfs(src, dest):
            visited = set()
            queue = deque()
            queue.append((src, 1))

            while queue:
                node, cur_val = queue.popleft()

                if node in visited:
                    continue
                visited.add(node)

                for nei, val in adj[node]:
                    if nei == dest:
                        return cur_val * val
                    else:
                        queue.append((nei, cur_val*val))

            return -1 

        answer = []
        for u, v in queries:
            if u not in adj or v not in adj:
                answer.append(-1)
            elif u == v :
                answer.append(1)
            else:
                answer.append(bfs(u, v))

        return answer


        