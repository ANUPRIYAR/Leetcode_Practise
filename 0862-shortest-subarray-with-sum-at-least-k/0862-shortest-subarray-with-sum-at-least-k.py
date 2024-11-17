from heapq import heappop as hpop , heappush as hpush
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        minlength = float('inf')
        stack = [(0, -1)]
        cumsum = 0

        for i in range(len(nums)):
            cumsum += nums[i]

            while stack and cumsum <= stack[-1][0]:
                stack.pop()

            stack.append((cumsum, i))

            index = self.binary_search(stack, cumsum - k)

            if index != -1:
                minlength = min(minlength, i - stack[index][1])


        return minlength if minlength != float('inf') else -1 

    def binary_search(self, stack, target):
        left = 0
        right = len(stack)-1

        while left <= right:
            mid = (left + right)//2

            if stack[mid][0]  <= target:
                left = mid + 1
            else:
                right = mid - 1


        return right 


