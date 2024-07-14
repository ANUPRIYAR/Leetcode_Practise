class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid) , len(grid[0])

        ps = [[0]*cols for _ in range(rows)]
        for i in range(rows):                   # calculating prefix sum matrix
            for j in range(cols):
                x = ps[i-1][j] if i > 0 else 0
                y = ps[i][j-1] if j > 0 else 0
                prev = ps[i-1][j-1] if (i > 0 and j > 0) else 0
                ps[i][j] = x + y - prev + grid[i][j]

        count = 0
        for i in range(rows):                                 # In the prefix sum matrix, all the elements whose value is less than k will be a matrix
            for j in range(cols) :                            # containing top-left element and value less than(or equal) k
                if ps[i][j] <= k :
                    count += 1

        return count

        
        
