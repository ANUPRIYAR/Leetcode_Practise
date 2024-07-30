class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = end = 0
        maxlen = 0
        n = len(nums)
        k_set = set()

        zeros = 0
        while end < n:
            num = nums[end]

            if num == 0:
                zeros += 1

            while zeros > k:
                if nums[start] == 0:
                    zeros -= 1

                start += 1


            length = end - start +  1
            maxlen = max(maxlen, length)
            end += 1

        return maxlen
                




           