class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int: 
        nums.sort()
        count = 0
        for i in range(len(nums)):
            smallest_index = self.find_lower_bound(nums, i +1, len(nums)-1, lower-nums[i])
            highest_index = self.find_lower_bound(nums, i +1, len(nums)-1, upper + 1-nums[i])

            count += highest_index - smallest_index 

        return count



    def find_lower_bound(self, arr, left, right, target):
        
        while left <= right:
            mid = (left + right)//2
            
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

      