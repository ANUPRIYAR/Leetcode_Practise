class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        if nums[len(nums)-1] > nums[0]:
            increasing = True
        else:
            increasing= False

        for i in range(1,len(nums)):
            if increasing:
                if nums[i] < nums[i-1]:
                    return False
            else:
                if nums[i] > nums[i-1]:
                    return False

        return True
        