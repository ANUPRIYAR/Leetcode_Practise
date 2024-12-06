class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)] 
        rows, cols = len(board), len(board[0])
        row, col = click
        visited = set()
        output = board.copy()
        
        if output[row][col] == 'M':
            output[row][col] = 'X'
            return output

        queue = deque()
        queue.append((row, col))
        visited.add((row, col))

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                adjacent_mine = 0
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if output[nx][ny] == 'M':
                            adjacent_mine += 1
                    
                if adjacent_mine > 0:
                    output[x][y] = str(adjacent_mine)
                else:
                    output[x][y] = 'B'
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                            queue.append((nx, ny))
                            visited.add((nx, ny))

        return output

                    




        