class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        cnt = [0 for _ in range(n + 1)]
        s = k = 0
        for i in range(n):
            while s + cnt[i] < nums[i]:
                k += 1
                if k - 1 >= len(queries): return -1
                l, r, val = queries[k - 1]
                if r < i: continue
                cnt[max(l, i)] += val
                cnt[r + 1] -= val
            s += cnt[i]
        return k