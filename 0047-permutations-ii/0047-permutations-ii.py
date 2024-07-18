class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permute_backtrack(current, freq, result):
            if len(current) == len(nums):
                # if current not in result:
                result.append(current[:])
                return 


            for i in range(len(nums)):
                if i > 0 and nums[i]==nums[i-1]:
                    continue
                if freq[i] == 0:
                    current.append(nums[i])
                    freq[i] = 1
                    permute_backtrack(current, freq, result)
                    current.pop()
                    freq[i] = 0

        result = []
        freq = dict.fromkeys(range(0,len(nums)), 0)
        permute_backtrack([], freq, result)
        return result


                
        