class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        count = 0
        for i in range(len(nums)):
            smallest_index = self.binary_search(nums, i + 1, len(nums) - 1, lower - nums[i])
            highest_index = self.binary_search(nums, i + 1, len(nums) - 1, upper + 1 - nums[i])
            count += highest_index - smallest_index
        return count

    
    def binary_search(self, array, left, right, target):
         
        while left <= right:
            mid = ( left + right)//2

            if array[mid] < target:
                left = mid + 1
            else:
                right  = mid -1 

        return right

        

