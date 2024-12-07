class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canAchieve(maxBalls):
            operations = 0
            for balls in nums:
                if balls > maxBalls:
                    # Calculate how many new bags are needed
                    # We need (balls - 1) // maxBalls additional bags
                    operations += (balls - 1) // maxBalls
                if operations > maxOperations:
                    return False
            return True

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if canAchieve(mid):
                right = mid  # Try for a smaller maximum penalty
            else:
                left = mid + 1  # Increase minimum penalty

        return left