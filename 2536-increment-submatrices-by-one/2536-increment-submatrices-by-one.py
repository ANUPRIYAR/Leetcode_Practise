class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]

        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2 + 1):
                mat[r][c1] += 1
                if c2 + 1 < n:
                    mat[r][c2 + 1] -= 1

        for r in range(n):
            for c in range(1, n):
                mat[r][c] += mat[r][c-1]


        return mat





        