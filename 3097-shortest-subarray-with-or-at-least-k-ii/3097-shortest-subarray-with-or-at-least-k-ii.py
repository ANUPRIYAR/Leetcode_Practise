class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float('inf')
        start = window = 0
        bits = [0] * 32
        for end in range(len(nums)):
            window |= nums[end]
            for i in range(32):
                if nums[end] & (1 << i):
                    bits[i] += 1
        
            while start <= end and window >= k:
                res = min(res, end - start + 1)
                for i in range(32):
                    out = nums[start] & (1 << i)
                    # print(f"{nums[start]} & {1 << i} : {out}")
                    if out:
                        bits[i] -= 1
                        if bits[i] == 0:
                            window ^= 1 << i
                start += 1
        return res if res < float('inf') else -1