class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index, result, current):
            if index == len(nums):
                result.append(current[:])
                return


            # pick this
            current.append(nums[index])
            backtrack(index + 1, result, current)
            current.pop()

            # not pick this 
            backtrack(index + 1, result, current)


        result = []
        backtrack(0, result, [])
        return result
        
        