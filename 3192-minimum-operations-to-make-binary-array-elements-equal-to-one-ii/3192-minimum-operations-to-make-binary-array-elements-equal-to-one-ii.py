class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        flips = 0
        for i in range(n):
            if nums[i] == 0 and flips % 2 == 0:
                flips += 1
            elif nums[i] == 1 and flips % 2 == 1:
                flips += 1

        return flips
            
        