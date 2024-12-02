class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def bfs(r, c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))

            while queue:
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == "1":
                        visited.add((nx, ny))
                        queue.append((nx, ny))


        num_islands = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1" and (x, y) not in visited:
                    num_islands += 1
                    bfs(x, y)

        return num_islands






            


        