class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 1), (0, 1), (1, 1)]
        moves = 0

        dp = [[-1] * cols for _ in range(rows)]

        def dfs(r, c):
            if dp[r][c] != -1:
                return dp[r][c]

            max_moves = 0

            for dr, dc in directions:
                nr, nc = r+ dr, c + dc

                if 0 <= nr < rows and  0 <= nc < cols and grid[nr][nc] > grid[r][c]:
                    # print(grid[r][c]  ,  grid[nr][nc])
                    max_moves = max(max_moves, dfs(nr, nc))

            
            dp[r][c] = max_moves + 1
            return dp[r][c]


        result = 0
        for r in range(rows):
            result = max(result, dfs(r, 0))

        return result - 1 if result > 0 else result

        
        