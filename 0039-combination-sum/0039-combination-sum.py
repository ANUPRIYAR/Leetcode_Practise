class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(index, result, current, target):
            # Base condition
            if  index == len(candidates):
                if target == 0:
                    print(current)
                    result.append(current[:])
                return 

            # take this
            if candidates[index] <= target:
                current.append(candidates[index])
                target -= candidates[index]
                backtrack(index, result, current, target)

                # backtrack
                current.pop()
                target += candidates[index]

            # skip this 
            backtrack(index + 1, result, current, target)

        result = []
        backtrack(0, result, [], target)
        return result


    

        