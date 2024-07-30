class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.find_count(nums, k) - self.find_count(nums, k-1)


    def find_count(self, nums, k):
        start, end = 0, 0
        hashmap = {"odd" : 0}
        count = 0
        n = len(nums)
        if k < 0:
            return 0

        while end < n :
            num = nums[end]
            if num & 1 != 0:
                hashmap["odd"] += 1
            
            while hashmap["odd"] > k:
                start_num = nums[start]
                if start_num & 1 != 0:
                    hashmap['odd'] -= 1

                start += 1

            count += (end - start + 1)
            end += 1

        return count
        