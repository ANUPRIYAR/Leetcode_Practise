class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def helper(bagsize):
            operations = 0
            for ballcount in nums:
                operations += math.ceil(ballcount/bagsize) - 1
                if operations > maxOperations:
                    return False

            return True

        left = 1
        right = max(nums)

        while left <= right:
            mid = left + (right - left)//2
            if helper(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left