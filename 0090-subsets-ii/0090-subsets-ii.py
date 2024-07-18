class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index, result, current):
            result.append(current[:])

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                backtrack(i+1, result, current)
                current.pop()

                # backtrack(i + 1, result, current)

        result = []
        nums.sort()
        backtrack(0, result, [])
        return result