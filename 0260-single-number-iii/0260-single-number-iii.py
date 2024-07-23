class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # find xor of all numbers
        xor = 0
        for num in nums:
            xor ^= num


        # find the right most set bit 
        rmst = 1
        while rmst & xor == 0:
            rmst <<= 1

        # if rightmost set bit & num is 0 then grp1 else grp2
        grp1= grp2 = 0

        for num in nums:
            if rmst & num == 0:
                grp1 ^= num
            else:
                grp2 ^= num

        return grp1, grp2

