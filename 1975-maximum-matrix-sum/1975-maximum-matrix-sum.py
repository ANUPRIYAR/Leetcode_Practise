class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negative_values = 0
        absolute_sum = 0
        minimum = float('inf')

        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                absolute_sum += abs(matrix[i][j])
                minimum = min(minimum, abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    negative_values += 1



        if negative_values % 2 == 0:
            return absolute_sum

        return absolute_sum - 2*(minimum)
        