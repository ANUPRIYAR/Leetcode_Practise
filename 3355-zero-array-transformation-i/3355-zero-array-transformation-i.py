class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        count = [0 for _ in range(n+1)]

        sum_ = 0
        k = 0

        for i in range(n):
            while sum_ + count[i] < nums[i]:
                k += 1
                if k - 1>= len(queries):
                    return False

                left, right = queries[k - 1]
                if right < i:
                    continue

                count[max(left, i)] += 1  # applying sweep line
                count[right + 1] -= 1

            sum_ += count[i]
        return k <= len(queries)
