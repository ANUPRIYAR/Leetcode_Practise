from collections import defaultdict
class Solution:
    def __init__(self):
        self.prime_dict = defaultdict(list)
        
    def minOperations(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        operations = 0

        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i + 1]:
                gpd = self.least_prime(nums[i])
                if gpd == -1 or gpd >= nums[i]:
                    return -1 
                nums[i] = gpd
                # while nums[i] > nums[i+1] and gpd < nums[i]:
                #     nums[i] //= int(gpd)
                operations += 1
                if nums[i] > nums[i+1] :
                    return -1


        return operations
                
    def least_prime(self, num):
        if num % 2 == 0:
            return 2
        for i in range(3, int(sqrt(num))):
            if num % i == 0:
                return i
        return -1

    # def FindPrimeNumbers(self, n):
    #     prime = [1]* (n + 1)
    #     prime[0] = prime[1] = 0
        
    #     for i in range(2, int(sqrt(n) + 1)):
    #         if prime[i] == 1:
    #             for j in range(i*i, n + 1, i):
    #                 prime[j] = 0

    #     prime_numbers = []
    #     for i in range(len(prime)):
    #         if prime[i] == 1:
    #             prime_numbers.append(i)
    #     self.prime_dict[n] = prime_numbers
        

    # def greatestproperdivisor(self, num):
    #     smallest_prime_factor = None
    #     if self.prime_dict.get(num, None) is None:
    #         self.FindPrimeNumbers(num)
    #     for key in self.prime_dict.keys():
    #         if num % key == 0:
    #             self.prime_dict[num] = self.prime_dict[key]

    #     prime_numbers = self.prime_dict[num]
    #     for prime in prime_numbers:
    #         if prime < num and num % prime == 0:
    #             smallest_prime_factor = prime
    #             break
        
    #     return smallest_prime_factor if smallest_prime_factor is not None else -1 
        




        