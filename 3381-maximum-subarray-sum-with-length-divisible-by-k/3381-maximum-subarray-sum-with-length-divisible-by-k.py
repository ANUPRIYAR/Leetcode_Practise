
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        seen  = defaultdict(lambda : float('inf'))
        seen[0] = 0
        prefix_sum = 0
        max_sum = - float('inf')

        for i in range(len(nums)):
            prefix_sum += nums[i]
            mod_index = (i+1) %  k

            if mod_index in seen:
                max_sum = max(max_sum, prefix_sum  - seen[mod_index])

            seen[mod_index] = min(seen[mod_index], prefix_sum)


        return max_sum




        