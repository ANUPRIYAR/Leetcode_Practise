class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        output = dict()

        for i in range(len(nums)):
            for j in range(len(nums)):
                and_out = nums[i] & nums[j]
                output[and_out] = output.get(and_out, 0) + 1

        ans  = 0
        for key, value in output.items():
            for num in nums:
                if num & key == 0:
                    ans += value


        return ans
                    
            

        
        
        