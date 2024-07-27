class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        cur_window_flips = 0
        res = 0
        n = len(nums)

        for i in range(n):
            #check if cur index is Out of Bounds for k size window
            if i - k >= 0 and nums[i -k] == 2:
                cur_window_flips -= 1    # then we reduce the effect of atleast 1 window which started at i-k index


            
            if (nums[i] + cur_window_flips)% 2 == 0:  
                if i + k > n:
                    return -1

                cur_window_flips += 1
                res += 1
                nums[i] = 2

        return res

        