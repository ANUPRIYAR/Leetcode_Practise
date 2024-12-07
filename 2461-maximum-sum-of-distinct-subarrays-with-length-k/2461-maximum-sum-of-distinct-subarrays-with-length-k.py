class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0
        max_sum = - float('inf')
        
        num_freq = dict()
        for num  in nums[:k]:
            num_freq[num] = num_freq.get(num, 0) + 1

        window_sum = sum(nums[:k])
        if len(num_freq) == k:
            max_sum = max(max_sum, window_sum)
        

        for end in range(len(nums) - k ):
            window_sum -= nums[end]
            window_sum += nums[end + k]

            # Remove first num from window
            num_freq[nums[end]] -= 1
            if num_freq[nums[end]] == 0 : del num_freq[nums[end]]
            # Add current num
            num_freq[nums[end + k]] = num_freq.get(nums[end + k], 0) + 1

            if len(num_freq) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum if max_sum != -float('inf') else 0
 


        