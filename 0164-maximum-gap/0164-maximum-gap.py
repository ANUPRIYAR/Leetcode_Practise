
import heapq

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        minheap = []
        for num in nums:
            heapq.heappush(minheap, num)

        max_diff = float(-inf)
        while minheap:
            num1 = heapq.heappop(minheap)

            if minheap:
                max_diff = max(max_diff, (minheap[0] - num1))

        return max_diff



        