class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        old_color = grid[row][col]
        visited = set()
        borders = set()

        def dfs(r, c):
            visited.add((r, c))
            is_border = False

            for dr, dc in directions:
                nr, nc = r + dr , c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] != old_color:
                        is_border = True
                    elif (nr, nc) not in visited:
                        dfs(nr, nc)

                else:
                    is_border = True 

            if is_border:
                borders.add((r, c))


        dfs(row, col)
        for r,c in borders:
            grid[r][c] = color

        return grid

        