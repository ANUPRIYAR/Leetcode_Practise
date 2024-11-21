class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        count = [0] * (n + 1)
        sum_ = 0
        q_index = 0


        for i in range(n):
            while sum_ + count[i] < nums[i]:
                # get query
                q_index += 1
                print(q_index)
                if q_index - 1 >= len(queries) :
                    return -1
                left, right , val = queries[q_index-1] 
                if right < i :
                    continue
                count[max(left, i)] += val
                count[right + 1 ] -= val

            sum_ += count[i] 
        return q_index 
        