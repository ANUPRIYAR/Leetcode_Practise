class Solution:
    def solve(self, col, board, count, leftrow, upperdiag, lowerdiag, n):
        if col == n:
            return 1
        c = 0
        for row in range(n):

            if leftrow[row] == 0 and upperdiag[row + col] == 0 and lowerdiag[n-1+col-row] == 0:
                board[row] = board[row][:col] + 'Q' + board[row][col + 1:]
                leftrow[row] = 1
                upperdiag[row + col] = 1
                lowerdiag[n-1+col-row] = 1
                c += self.solve(col +1,board, count , leftrow, upperdiag, lowerdiag, n)
                board[row] = board[row][:col] + '.' + board[row][col + 1:]
                leftrow[row] = 0
                upperdiag[row + col] = 0
                lowerdiag[n-1+col-row] = 0


        return c










    def totalNQueens(self, n: int) -> int:
        count = 0
        board = [ '.'*n for _ in range(n)]
        leftrow = [0]*n
        upperdiag = [0]*(2*n-1)
        lowerdiag = [0]*(2*n-1)
        return self.solve(0, board, count, leftrow, upperdiag, lowerdiag, n)




        