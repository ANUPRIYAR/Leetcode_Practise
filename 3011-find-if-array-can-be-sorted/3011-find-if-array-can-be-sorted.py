class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        start = 0
        for end in range(1, len(nums)):
            if self.count_setbits(nums[end]) != self.count_setbits(nums[end - 1]):
                previous_max = max(nums[start:end])
                j = end
                while j < len(nums)-1 and self.count_setbits(nums[j]) == self.count_setbits(nums[j+1]):
                    j += 1
                
                currentmin = min(nums[end: j+1])
                if previous_max > currentmin:
                    return False

                start = end
               

        return True

    def count_setbits(self, num):
        count = 0
        while num > 0:
            count += num & 1
            num >>= 1

        return count
        