class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        dist = [[sys.maxsize]* cols for _ in range(rows)]
        dist[0][0] = 0

        queue.append((0, 0))

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0<= ny < cols:
                    d = dist[x][y] + grid[nx][ny]
                    if d < dist[nx][ny]:
                        dist[nx][ny] = d

                        if grid[nx][ny] == 0:
                            queue.appendleft((nx, ny))
                        else:
                            queue.append((nx, ny))


        return dist[rows-1][cols - 1]



        
        