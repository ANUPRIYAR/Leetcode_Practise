class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        borders = set()
        oldcolor = grid[row][col]

        def bfs(r, c):

            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            is_border = False

            while queue:
                x, y  = queue.popleft()

                is_border = False
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols:
                        if grid[nx][ny] != oldcolor:
                            is_border = True
                        elif (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                    else:
                        is_border = True

                if is_border:
                    borders.add((x, y))


        bfs(row, col)

        for r, c in borders:
            grid[r][c] = color

        return grid