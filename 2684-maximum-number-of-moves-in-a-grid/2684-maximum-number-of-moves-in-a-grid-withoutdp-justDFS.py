class Solution:
    def __init__(self):
        self.directions = [(-1, 1), (0, 1), (1, 1)]
        
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        max_moves = 0
        for row in range(rows):
            max_moves = max(max_moves, self.dfs(row, 0 ,grid,  0, set()))
        return max_moves


    def dfs(self, x, y, grid, moves, visited):
        visited.add((x, y))
        moves = 0
        for dx, dy in self.directions:
            if 0<= x + dx < len(grid) and 0<= y + dy < len(grid[0]) and grid[x+dx][y+dy] > grid[x][y] and (x+dx, y+dy) not in visited:
                moves = max(moves, 1 + self.dfs(x+dx, y +dy, grid, moves, visited))


        return moves 



        
