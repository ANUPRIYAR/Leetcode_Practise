from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for (u, v), value in zip(equations, values):
            adj[u].append([value, v])
            adj[v].append([1/value, u])

        
        def dfs(node, destination, visit):
            
            if node == destination:
                return 1.0
            visit.add(node)

            for value, child in adj[node]:
                if child not in visit:
                    product = dfs(child, destination, visit,)
                    if product != -1:
                        return product * value


            visit.remove(node)
            return -1.0

        
        result = []
        for source, destination in queries:
            if source not in adj or destination not in adj:
                result.append(float(-1))
            elif source == destination:
                result.append(float(1))
            else:
                result.append(dfs(source, destination, set()))

        return result


                




        





        
        