class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        x_map = {"X": 1}
        y_map = {"Y": 1}
        ps = [[0]* cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                x = ps[i-1][j] if i > 0 else [0, 0]
                y = ps[i][j-1] if j > 0 else [0, 0]
                prev = ps[i-1][j-1] if (i > 0 and j > 0) else [0,0]
                x_value = x[0] + y[0] - prev[0] + x_map.get(grid[i][j], 0)
                y_value = x[1] + y[1]- prev[1] + y_map.get(grid[i][j], 0)
                ps[i][j] = [x_value, y_value]
        print(ps)

        count = 0
        for i in range(rows):
            for j in range(cols):
                x, y = ps[i][j][0], ps[i][j][1]
                if x == y and x > 0:
                    count += 1
        return count