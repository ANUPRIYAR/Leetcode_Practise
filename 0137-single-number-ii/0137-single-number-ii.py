class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans  = 0
        is_neg = 0
        for i in range(32):
            count = 0
            for j in range(len(nums)):
                if nums[j] < 0:
                    is_neg = is_neg + 1
                
                if abs(nums[j]) & (1<<i):
                    count += 1
                    
            if count % 3 == 1:
                ans = ans | (1 << i)
        if is_neg %3 != 0:
            return -ans
        return ans
