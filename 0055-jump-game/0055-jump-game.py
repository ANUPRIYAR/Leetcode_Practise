class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_index = 0
        for cur in range(len(nums)):
            if cur > max_index :
                return False
            max_index = max(max_index, cur + nums[cur])

        return True

        