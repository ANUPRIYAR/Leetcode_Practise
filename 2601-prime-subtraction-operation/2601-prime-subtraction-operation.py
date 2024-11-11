class Solution:
    def __init__(self):
        self.primenumbers = []

    def primeSubOperation(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        max_num = max(nums)
        self.findprimes(max_num)

        index = self.find_max_subtraction(self.primenumbers, 0, nums[0])
        if index != -1:
            nums[0] -= self.primenumbers[index]
        
        
        for i in range(1, len(nums)):
            index = self.find_max_subtraction(self.primenumbers, nums[i-1], nums[i])

            if index == -1 and nums[i] <= nums[i-1]:
                return False
            elif index != -1:
                nums[i] -= self.primenumbers[index]
            
            # if nums[i-1] > nums[i]:
            #     if i != 1:
            #         prev = nums[i-2]
            #     index = self.find_max_subtraction(self.primenumbers, prev, nums[i-1])
                 
            #     if index != -1:
            #         nums[i-1] -= self.primenumbers[index]
            #     else:
            #         return False
            #     print(nums)

        return True


    def find_max_subtraction(self, primes, prev, current):
        if len(primes) == 0 or primes[0] >= current:
            return -1

        if prev == -1:
            p = len(primes) - 1
            while p > 0 and primes[p] >= current:
                p -= 1
            return p

        left = 0
        right = len(primes) - 1
        
        print(primes)
        while left <= right:
            mid = left + (right - left)//2

            if current - primes[mid] <= prev:
                right = mid - 1
            else:
                if mid == len(primes) - 1 or current - primes[mid + 1] <= prev:
                    return mid
                else:
                    left = mid + 1
            
                
        # print(f"current: { current}")
        # print(f"primes[left] : {primes[left]}")
        # if current - primes[left] <= prev:
        #     return -1
        
        return -1 if right >=0  and current - primes[right] <= prev else right


    def findprimes(self, num):
        prime = [1]* (num + 1)
        prime[0] = prime[1] = 0

        # if self.primenumbers.get(num, None) is not None:
        #     return

        for i in range(2, int(sqrt(num)) + 1):
            if prime[i] == 1:
                for j in range(i*i, num + 1, i):
                    prime[j] = 0
            
        for i in range(len(prime)):
            if prime[i] == 1:
                self.primenumbers.append(i)