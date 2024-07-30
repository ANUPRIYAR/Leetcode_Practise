class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.find_count(nums, k) - self.find_count(nums, k-1)


    def find_count(self, nums, k):
        start, end, n = 0, 0, len(nums)
        odds, count = 0, 0

        if k < 0:
            return 0

        while end < n :
            num = nums[end]
            if num & 1 != 0:
                odds += 1
            
            while odds > k:
                start_num = nums[start]
                if start_num & 1 != 0:
                    odds -= 1
                start += 1

            count += (end - start + 1)
            end += 1

        return count
        