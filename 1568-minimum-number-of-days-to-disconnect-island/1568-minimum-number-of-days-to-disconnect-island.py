directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        sep_info = self.IslandInfo(False, 0)
        total_land, total_island = 0, 0

        discovery_time = [[-1]*cols for _ in range(rows)]
        low = [[-1]*cols for _ in range(rows)]
        parent = [[-1]* cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    total_land += 1
                    if discovery_time[row][col] == -1:
                        self.findcriticalpoints(grid, row, col, discovery_time, low, parent, sep_info)
                        total_island += 1

        if total_island == 0 or total_island >= 2: return 0   # Already disconnected or no land
        if total_land == 1: return 1 # only 1 land cell present
        if sep_info.hasCriticalPoint: return 1
        return 2


    def findcriticalpoints(self, grid, row, col, discovery_time, low, parent, sep_info):
        rows, cols = len(grid), len(grid[0])
        discovery_time[row][col] = low[row][col] = sep_info.discoverytime
        sep_info.discoverytime += 1
        
        children = 0

        for dx, dy in directions:
            newrow = row + dx
            newcol = col + dy
            if 0 <= newrow < rows and 0 <= newcol < cols and grid[newrow][newcol] == 1:
                if discovery_time[newrow][newcol] == -1:
                    children += 1
                    parent[newrow][newcol] = row*cols + col
                    self.findcriticalpoints(grid, newrow, newcol, discovery_time, low, parent, 
                    sep_info)

                    low[row][col] = min(low[row][col], low[newrow][newcol])

                    if low[newrow][newcol] >= discovery_time[row][col] and parent[row][col] != -1:
                         sep_info.hasCriticalPoint = True
                elif newrow* cols + newcol  != parent[row][col]:
                    low[row][col] = min(low[row][col], discovery_time[newrow][newcol])



        if parent[row][col] == -1 and children > 1:
            sep_info.hasCriticalPoint = True


    class IslandInfo:
        def __init__(self,hasCriticalPoint: bool, discoverytime ):
            self.hasCriticalPoint = hasCriticalPoint
            self.discoverytime = discoverytime




        