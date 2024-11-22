class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = dict()

        for row in matrix:
            pattern =  [cell if row[0] == 0 else cell^ 1 for cell in row]
            pattern = ''.join(str(pattern))
            patterns[pattern] = patterns.get(pattern, 0) + 1

        return max(patterns.values())
