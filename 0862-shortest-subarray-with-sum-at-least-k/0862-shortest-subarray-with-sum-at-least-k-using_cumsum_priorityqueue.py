from heapq import heappop as hpop , heappush as hpush
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        minlength = float('inf')
        minheap = []
        cum_sum = 0

        for i, num in enumerate(nums):
            cum_sum += num

            if cum_sum >= k:
                minlength = min(minlength, i + 1)

            while minheap and cum_sum - minheap[0][0] >= k:
                minlength = min(minlength, i - hpop(minheap)[1])

            hpush(minheap, (cum_sum, i))

        return minlength if minlength != float('inf') else -1 


