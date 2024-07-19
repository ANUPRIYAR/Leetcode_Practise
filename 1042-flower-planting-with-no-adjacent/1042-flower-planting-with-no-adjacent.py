class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in paths:
            graph[a].append(b)
            graph[b].append(a)

        if paths == []:
            return [1]*n

        def backtrack(node, color_map):
            if node == n + 1:
                return True

            for i in range(1, n +1):
                if self.is_safe(node, i, color_map, graph):
                    color_map[node] = i
                    print(f"coloured node { node} as {i}")
                    if backtrack(node + 1, color_map):
                        return True
                    print(f"backtracking node: {node}")
                    color_map[node] = 0

            return False


        color_map = dict.fromkeys(range(1, n+1), 0)
        backtrack(1, color_map)
        print(f"color_map: {color_map}")
        res = []
        for key in color_map:
            res.append(color_map[key])

        return res

    def is_safe(self, node, color, color_map, graph):
        for child in graph[node]:
            if color_map[child] == color:
                return False
        return True

            

                     



                        
                



        

        

        
        