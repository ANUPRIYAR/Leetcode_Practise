class Solution:
    def smallestNumber(self, n: int) -> int:
        cur = n
        numbits = 0
        while cur > 0:
            numbits += 1
            cur >>= 1

        allsetbits = ( 1 << numbits) - 1
        return allsetbits
            

        
        