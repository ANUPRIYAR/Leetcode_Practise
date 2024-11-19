class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        begin = 0
        freq = dict()
        window_sum = 0
        max_sum = 0

        for end in range(len(nums)):
            freq[nums[end]] = freq.get(nums[end], 0) + 1
            window_sum += nums[end]

            while freq[nums[end]] > 1 or end - begin + 1 > k:
                freq[nums[begin] ] -= 1
                window_sum -= nums[begin]
                begin += 1

            if end - begin + 1 == k:
                max_sum = max(max_sum, window_sum)


        return max_sum
            





