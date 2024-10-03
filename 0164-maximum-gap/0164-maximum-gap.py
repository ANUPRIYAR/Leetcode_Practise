
import heapq

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        self.radix_sort(nums)
        max_gap = 0
        if len(nums) < 2:
            return 0

        maxheap = []
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            heapq.heappush(maxheap, - diff)


        return -heapq.heappop(maxheap)


    def radix_sort(self, nums):
        max_val = max(nums)

        exp = 1
        while max_val//exp > 0:
            self.counting_sort(nums, exp)
            exp *= 10
        

    def counting_sort(self, nums, exp):
        count = [0] * 10
        output = [0] * len(nums)

        # count freqeuncy
        for num in nums:
            digit = (num//exp)% 10
            count[digit] += 1


        #  cumulative freqeuncy
        for i in range(1, len(count)):
            count[i] += count[i-1]

        # Update output
        for i in range(len(nums) - 1, -1, -1):
            digit = (nums[i]//exp)% 10
            output[count[digit] - 1] = nums[i]
            count[digit] -= 1

        # reset nums
        for i in range(len(nums)):
            nums[i] = output[i]



        
        