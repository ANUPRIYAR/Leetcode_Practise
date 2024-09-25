from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start = 0
        max_length = 0

        min_queue = deque()
        max_queue = deque()

        
        for end in range(len(nums)):
            while min_queue and nums[min_queue[-1]] >= nums[end]:
                min_queue.pop()
            min_queue.append(end)
            

            while max_queue and nums[max_queue[-1]] <= nums[end]:
                max_queue.pop()
            max_queue.append(end)
            # print(f"window : {nums[start:end]}")
            # print(f"min_queue: {min_queue}")
            # print(f"max_queue: {max_queue}")

            while min_queue and max_queue and  (nums[max_queue[0]] - nums[min_queue[0]] > limit):
                print(f"inside invalid")
                start += 1

                if min_queue[0] < start:
                    min_queue.popleft()

                if max_queue[0] < start:
                    max_queue.popleft()
       
            max_length = max(max_length, end - start + 1)

        return max_length
                
                





        