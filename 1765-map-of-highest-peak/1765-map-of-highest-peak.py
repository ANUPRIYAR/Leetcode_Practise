class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(isWater), len(isWater[0])
        queue = deque()
        output = [[-1]* cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    output[i][j] = 0
                    queue.append((i, j))
                    


        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx , y + dy
                if 0 <= nx < rows and 0 <= ny < cols and output[nx][ny] == -1:
                    output[nx][ny] = output[x][y] + 1
                    queue.append((nx, ny))


        return output


        
                
        