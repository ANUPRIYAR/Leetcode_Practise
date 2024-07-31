class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.find_count(nums, k) - self.find_count(nums, k-1)


    def find_count(self, nums, k):
        n = len(nums)
        start, end, count = 0, 0, 0
        hashmap = dict()

        if k < 0:
            return 0

        while end < n:
            num = nums[end]
            hashmap[num] = hashmap.get(num, 0) + 1

            while len(hashmap) > k:
                startnum = nums[start]
                hashmap[startnum] -= 1
                if hashmap[startnum] == 0:
                    del hashmap[startnum]
                start += 1

            
            count += end - start + 1
            end += 1
        return count


        