from collections import deque
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        minque = deque()
        maxque = deque()

        n = len(nums)
        start = 0
        count = 0
        for end in range(n):

            while minque and nums[minque[-1]] >= nums[end]:
                minque.pop()
            minque.append(end)

            while maxque and nums[maxque[-1]] <= nums[end]:
                maxque.pop()
            maxque.append(end)


            while maxque and minque and nums[maxque[0]] - nums[minque[0]] > 2:
                start += 1

                if minque[0] < start:
                    minque.popleft()

                if maxque[0] < start:
                    maxque.popleft()


            count += (end- start + 1)

        return count 


        