class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0]* n for _ in range(m)]
        
        # guards and walls = 2
        for i, j in guards:
            grid[i][j] = 2

        for i, j in walls:
            grid[i][j] = 2


        # Mark Guaraded as -1 
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for gx, gy in guards:
            for dx, dy in directions:
                x, y = gx, gy
                while True:
                    x += dx
                    y += dy
                    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 2:
                        break

                    grid[x][y] = -1

        # Count unguarded cells still marked as 0
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    ans += 1

        return ans

                    


        

        

