class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = [[0, 0] for _ in range(rows*cols)]
        numvisited = 0
        dx, dy = 0, 1 # starts with right direction
        directionchange = 0

        while numvisited < (rows * cols):
            for step in range((directionchange//2) + 1):
                if 0 <= rStart < rows and 0 <= cStart < cols: 
                    result[numvisited] = [rStart, cStart]
                    numvisited += 1

                rStart += dx
                cStart += dy

            # Direction change
            temp = dx
            dx = dy
            dy = - temp
            directionchange += 1

        return result

        