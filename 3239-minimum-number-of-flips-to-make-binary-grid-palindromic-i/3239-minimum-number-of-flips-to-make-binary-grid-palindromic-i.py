class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        rowflips, colflips = 0, 0

        for i in range(rows):
            for j in range(cols//2):
                if grid[i][j] != grid[i][cols - j -1]:
                    colflips += 1

        for j in range(cols):
            for i in range(rows//2):
                if grid[i][j] != grid[rows-i-1][j]:
                    rowflips += 1


        return min(colflips, rowflips)


        