class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        answer = [-1]* (len(nums) - k + 1)

        if len(nums) == 1 and k == 1:
            return nums
        
        if k == 1:
            return nums

        consecutive = 1

        for end in range(1, len(nums)):
            if nums[end] -1 == nums[end - 1]:
                consecutive += 1
            else:
                consecutive = 1

            if consecutive == k:
                answer[end - k + 1] = nums[end]
                consecutive -= 1

        return answer




        