class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        max_outlier = - float('inf')
        possible_outlier = None
        freq = Counter(nums)
        
        for i in range(len(nums)):
            currsum = total_sum - nums[i]
            if currsum % 2 == 0:
                possible_sum = currsum//2
                if possible_sum in freq and (freq[possible_sum] >= 2 or possible_sum != nums[i]):
                    possible_outlier = nums[i]
                    max_outlier = max(max_outlier, possible_outlier )
                    
        return max_outlier 