class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        count = [0]* n 

        for query in queries:
            count[query[0]] += 1
            if query[1] + 1 < n:
                count[query[1] + 1] -= 1 

        
        curfreq = 0
        for i in range(n):
            # cumulative sum until i
            curfreq += count[i]
            if curfreq < nums[i]:
                return False

        return True 
        