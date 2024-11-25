class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        peri = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()


        def bfs(r, c):
            nonlocal peri
            queue = deque([(r, c)])
            visited.add((r, c))

            while queue:
                x, y = queue.popleft()

                for dx, dy in directions:
                    nr, nc = x + dx , y + dy

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 0:
                            peri += 1

                        elif (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append((nr, nc))

                    else:
                        peri  += 1


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    bfs(i, j)
        return peri


        



        