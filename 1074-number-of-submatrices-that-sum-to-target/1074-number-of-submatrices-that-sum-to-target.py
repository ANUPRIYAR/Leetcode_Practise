class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        ps = [[0]* cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                x = ps[i-1][j] if i > 0 else 0
                y = ps[i][j-1] if j > 0 else 0
                prev = ps[i-1][j-1] if (i > 0 and j > 0) else 0
                ps[i][j] = x + y - prev + matrix[i][j]


        count = 0
        for r1 in range(rows):
            for r2 in range(r1, rows):
                sums = defaultdict(int)
                sums[0] = 1
                for c in range(cols):
                    curr_sum = ps[r2][c] - (ps[r1-1][c] if r1 > 0 else 0 )

                    count += sums[curr_sum - target]
                    sums[curr_sum] += 1
        return count
        

        




        