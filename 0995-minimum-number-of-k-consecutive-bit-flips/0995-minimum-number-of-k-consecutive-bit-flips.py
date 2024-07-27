class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        cur_window_flips = 0
        res = 0
        n = len(nums)

        for i in range(n):
            #check if cur index is Out of Bounds for k size window
            if i - k >= 0 and nums[i -k] == 2:
                cur_window_flips -= 1    # then we reduce the effect of atleast 1 window which started at i-k index


            # nums[i] is original element, and if  even flips-that means no change, odd flips- bit flipped, 
            # We know, the window starts when even after flips , the number is 0,
            # So if orig was 0 and 1 flip done. it means now its 1, so NO CHANGE reqd so mathematically. (0 + 1) % 2 == 1
            # But if orig was 1 and 1 flip done(so now 0) OR orig was 0 and 2 flips done (so now 0 only)... 
            # then Ist case: (1+1)%2 => 0 2nd Case: (0+2)%2 => 0 ... that means (nums[i] + nflips) should have remainder 0, when window operation starts
            if (nums[i] + cur_window_flips)% 2 == 0:  
                if i + k > n:
                    return -1

                cur_window_flips += 1
                res += 1
                nums[i] = 2

        return res

        