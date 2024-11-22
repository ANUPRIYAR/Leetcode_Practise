class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        nums.sort(key=lambda x:(x[0], x[1]))
        print(nums)
        
        count = [0] * 102
        
        for start, end in nums:
            count[start] += 1
            count[end + 1] -= 1 
            # min_index = min(min_index, start)
            # max_index = max(max_index, end)


        cursum = 0
        counter = 0

        for i in range(1, 102 ):
            cursum += count[i]
            if cursum > 0:
                counter += 1

        return counter
        

        