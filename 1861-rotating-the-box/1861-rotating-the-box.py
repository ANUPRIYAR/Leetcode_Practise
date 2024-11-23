class Solution:
    def rotateTheBox(self, grid: List[List[str]]) -> List[List[str]]:
        rows, cols = len(grid), len(grid[0])

        for x in range(rows-1, -1, -1):
            for y in range(cols):
                if grid[x][y] == '.'  and grid[x][y-1] == '#':
                    dx, dy = 0, -1
                    px, py = x, y
                    nx, ny = x +dx, y + dy
                    while True:
                        if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] == "*":
                            break
                        grid[px][py], grid[nx][ny] = grid[nx][ny], grid[px][py]
                        px, py = nx, ny
                        nx += dx
                        ny += dy


        # print(grid)

        # transposed = [list(row) for row in zip(*grid)]
        # rotated = [row[::-1] for row in transposed]
        matrix  = [[0]*rows for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                matrix[c][rows-r-1] = grid[r][c]


        return matrix

        
        