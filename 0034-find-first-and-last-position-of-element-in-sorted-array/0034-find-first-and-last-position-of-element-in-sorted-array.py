class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)

        return [left, right]

    def binary_search(self, nums, target, left_search_flag):
        left = 0
        right = (len(nums) - 1)
        idx = -1

        while left <= right:
            mid = left + (right  - left)//2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

            else:
                idx = mid
                if left_search_flag:
                    right = mid - 1
                else:
                    left = mid + 1
        return idx

        
