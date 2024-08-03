from collections import defaultdict

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        rows, cols = len(grid),len(grid[0])
        rowmap = [0]* rows
        colmap = [0]* cols

        ans  = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    rowmap[i] += 1
                    colmap[j] += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (rowmap[i] > 1 or colmap[j] > 1):
                    ans += 1


        return ans


                    

