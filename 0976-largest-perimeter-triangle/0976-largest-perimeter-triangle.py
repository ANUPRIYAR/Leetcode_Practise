class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        i = 0
        j = 1
        k = 2

        while k < len(nums):
            if nums[i] < nums[j] + nums[k]:
                return nums[i] + nums[j] + nums[k]
            else:
                k += 1
                j += 1
                i += 1
            
        return 0

        