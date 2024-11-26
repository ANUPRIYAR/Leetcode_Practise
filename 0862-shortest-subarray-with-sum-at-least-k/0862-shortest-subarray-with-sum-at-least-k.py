from heapq import heappush as hpush , heappop as hpop
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum
        minlength = float('inf')
        minheap = []
        for i in range(len(nums)):
            if i != 0:
                prefix_sum[i] += prefix_sum[i-1] + nums[i]
            else:
                prefix_sum[i] = nums[i]

            if prefix_sum[i] >= k:
                minlength = min(minlength, i + 1)

           
            while minheap and prefix_sum[i] - minheap[0][0] >= k:
                print(f"smallest :{minheap[0][0] }")
                cumsum, j = hpop(minheap)
                minlength = min(minlength, i - j )

            hpush(minheap, (prefix_sum[i], i))
            # print(minheap)


        return minlength if minlength != float('inf') else - 1
                

            



        


        

        