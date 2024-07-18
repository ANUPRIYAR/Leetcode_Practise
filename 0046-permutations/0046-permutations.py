class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def permute_backtrack(current, freq, result):
            if len(current) == len(nums):
                result.append(current[:])
                return 

            for i in range(len(nums)):
                if freq[i] == 0:
                    current.append(nums[i])
                    freq[i] = 1
                    permute_backtrack(current, freq, result)
                    current.pop()
                    freq[i] = 0


        freq = dict.fromkeys(range(0,len(nums)),0)
        result = []
        permute_backtrack([], freq, result)
        return result
        