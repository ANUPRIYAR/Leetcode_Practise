class Solution:
    def largestCombination(self, nums: List[int]) -> int:
        bit_counts = [0]*32

        for i in range(len(nums)):
            for j in range(32):
                if nums[i] & 1<<j != 0:
                    bit_counts[j] += 1


        return max(bit_counts)