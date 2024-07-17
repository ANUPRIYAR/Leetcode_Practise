class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(index, result, current, target):
            if target < 0 : return 
            
            if target == 0:
                if current not in result:
                    result.append(current[:])
                return 

            # pick this 
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] > target:
                    break
                index = i
                current.append(candidates[i])
                backtrack(i + 1, result, current, target - candidates[i])

                # backtracking
                current.pop()

        result = []
        candidates.sort()
        backtrack(0, result, [], target)
        return result