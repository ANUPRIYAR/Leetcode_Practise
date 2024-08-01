class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digits = [num  for num in nums  if num < 10]
        single_sum = sum(single_digits)
        sum_double = sum(nums) - single_sum
        if sum_double == single_sum:
            return False

        return True 

        