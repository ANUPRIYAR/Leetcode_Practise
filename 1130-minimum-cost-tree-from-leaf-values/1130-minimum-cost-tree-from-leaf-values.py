class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        return self.helper(arr, 0, len(arr) - 1 , {})

    def helper(self, arr, l, r , dp):
        if (l, r) in dp:
            return dp[(l, r)]

        if l >= r:
            return 0

        res = float('inf')

        for k in range(l, r):
            rootVal = max(arr[l:k + 1]) * max(arr[k + 1 : r + 1])
            res = min(res, rootVal + self.helper(arr, l, k, dp) + self.helper(arr, k + 1, r, dp))

        dp[(l, r)] = res

        return dp[(l, r)]
        