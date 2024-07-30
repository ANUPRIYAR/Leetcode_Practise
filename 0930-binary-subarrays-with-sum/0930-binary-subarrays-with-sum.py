class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.find_count(nums, goal) - self.find_count(nums, goal- 1)

    def find_count(self, nums, goal):
        start, end = 0, 0
        sum_, count = 0, 0
        n = len(nums)

        if goal < 0:
            return 0
        
        while end < n :
            sum_ += nums[end]

            while sum_ > goal:
                sum_ -= nums[start]
                start += 1

            count += (end - start + 1)

            end += 1
        return count

