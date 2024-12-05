class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i,( u, v) in enumerate(equations) :
            adj[u].append((v, values[i]))
            adj[v].append((u, 1/values[i]))


        def compute_graph(a, b):
            visited = set()

            queue = deque()
            queue.append((a, 1))

            while queue:
                node, cur_val = queue.popleft()

                if node in visited:
                    continue

                visited.add(node)

                for nei, val in adj[node]:
                    if nei == b:
                        return cur_val * val
                    else:
                        queue.append((nei, cur_val*val))

            return -1 

        answers = []
        for u, v in queries:
            if u not in adj or v not in adj:
                answers.append(-1) 
            elif u == v:
                answers.append(1)
            else:
                answers.append(compute_graph(u, v))

        return answers
                    
                    


        


        