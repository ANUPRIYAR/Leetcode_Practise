class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canAchieve(maxBalls):
            operations = 0
            for balls in nums:
                if balls > maxBalls:
                    operations += math.floor((balls - 1)/maxBalls)
                    if operations > maxOperations:
                        return False
            return True


        left = 1 
        right = max(nums)
        while left <= right:
            mid =  left + (right - left)//2
            if canAchieve(mid):
                right = mid -1 
            else:
                left = mid + 1
        return left
