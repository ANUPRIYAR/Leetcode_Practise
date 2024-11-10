class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        start = 0
        or_result = 0
        min_length = float('inf')
        bit_count = [0] * 32

        for end in range(len(nums)):
            or_result |= nums[end]
            for i in range(32):
                if nums[end] & 1<<i:
                    bit_count[i] += 1

            while start <= end and or_result >= k:
                min_length = min(min_length, end - start + 1)
                start_num = nums[start]
                for i in range(32) :
                    if start_num & 1<<i:
                        bit_count[i] -= 1
                        if bit_count[i] == 0:
                            or_result = 0
                            for i in range(32):
                                if bit_count[i] > 0:
                                    or_result += pow(2, i)
                start  += 1

        return min_length if min_length != float('inf') else -1 













        