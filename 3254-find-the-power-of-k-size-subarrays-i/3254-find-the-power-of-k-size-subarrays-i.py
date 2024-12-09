class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        answer = [-1]* (len(nums) - k + 1)
        consecutive = 1
        if k == 1:
            return nums
        
        for end in range(1,len(nums)):
            if nums[end] - 1 == nums[end -1]:
                consecutive += 1
            else:
                consecutive = 1
            # print(f"consecutive:{consecutive} end:{end}")
            if consecutive == k:
                answer[end - k + 1] = nums[end]
                # print(f"end - k + 1 : {end - k + 1}")
                consecutive -= 1

        return answer
            

        
        