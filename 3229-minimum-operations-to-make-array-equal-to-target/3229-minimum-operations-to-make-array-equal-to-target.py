class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        if len(nums) !=len(target):
            return -1

        diff  = [0] * len(nums)
        for i in range(len(nums)):
            diff[i] = target[i] - nums[i]

        operations = 0
        prev = 0
        for curr in diff:
            if (curr > 0 and prev < 0) or (curr < 0 and prev > 0):
                operations += abs(curr)

            elif abs(curr) > abs(prev):
                operations += abs(curr) - abs(prev)

            elif abs(curr) <= abs(prev):
                operations += 0

            prev = curr

        return operations

                




         
        
        
       
        
        