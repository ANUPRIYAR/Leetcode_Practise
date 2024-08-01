from math import sqrt
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:

        prime_numbers  = self.find_prime_range(l, int(sqrt(r) + 1))
        special_count = 0
        for prime in prime_numbers:
            if l <= prime * prime  <= r:
                special_count += 1

        non_special_count = (r -l + 1) - special_count
        return non_special_count


    def find_prime_range(self, l, r):
        prime = [1]* (r + 1)
        prime[0]= prime[1] = 0

        for i in range(2, int(sqrt(r) + 1)):
            if prime[i] == 1:
                for j in range(i*i , r + 1, i):
                    prime[j] = 0

        return [i for i in range(r+1) if prime[i] == 1]


       


    
        


        