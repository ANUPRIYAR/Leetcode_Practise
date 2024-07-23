class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # check if unset but if n is also unsert for k
        unset_bits = [1]*32
        for i in range(32):
            if n & 1<<i == 0:
                if k & 1 << i != 0:
                    return -1

        res = n ^ k
        count = 0
        while res >0 :
            res &= res -1 
            count += 1

        return count
            
                

        

        