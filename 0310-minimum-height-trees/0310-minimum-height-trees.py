class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if  n == 0:
            return []

        if n == 1:
            return [0]
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        
    
        def dfs_height(graph, node, visited):
            visited.add(node)
            max_height = 0
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    # Recursively calculate the height for each unvisited neighbor
                    current_height = dfs_height(graph, neighbor, visited)
                    max_height = max(max_height, current_height)

            # Return height as number of edges from this node to its deepest leaf
            return max_height + 1

        heights = {}
        height_map = defaultdict(list)
        for root in range(len(adj)):
            visited = set()
            height = dfs_height(adj, root, visited) - 1  # Subtracting one because we want edges count
            heights[root] = height
            height_map[height].append(root)
        print(heights)
        sorted_map = dict(sorted(height_map.items(), key = lambda x:x[0] ))
        key = list(sorted_map.keys())[0]
        return height_map[key]


    
       



