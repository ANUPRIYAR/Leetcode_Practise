from collections import defaultdict
class Solution:
    def __init__(self):
        self.solved = False
    
    def solve(self, rowmap, colmap, gridmap, grid, numbers):
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    id = self.get_id(row, col)
                    for num in numbers:
                        if num not in rowmap[row] and num not in colmap[col] and num not in gridmap[int(id)]:
                            grid[row][col] = num
                            # print(f"num updated : {num}")
                            rowmap[row].append(num)
                            colmap[col].append(num)
                            gridmap[id].append(num)
                            if self.solve( rowmap, colmap, gridmap, grid, numbers):
                                return True
                            # print(f"backtracking: {num}")
                            grid[row][col] = 0
                            rowmap[row].remove(num)
                            colmap[col].remove(num)
                            gridmap[id].remove(num)
                    return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        rowmap = defaultdict(list)
        colmap = defaultdict(list)
        gridmap = defaultdict(list)
        numbers = [1,2,3,4,5,6,7,8,9]

        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] != '.':
                    num = int(board[row][col])
                    rowmap[row].append(num)
                    colmap[col].append(num)
                    id = self.get_id(row, col)
                    gridmap[id].append(num)
                    board[row][col] = num
                else:
                    board[row][col] = 0
        
        # print(f"rowmap: {rowmap}")
        # print(f"colmap: {colmap}")
        # print(f"gridmap: {gridmap}")
        grid = board.copy()
        self.solve(rowmap, colmap, gridmap, grid, numbers)
        for row in range(rows):
            for col in range(cols):
                grid[row][col] = str(grid[row][col])
        return grid


    def get_id(self, row, col):
        r = row//3
        c = col//3
        id = 3*r + c
        return id