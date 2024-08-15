from heapq import heappush, heappop
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        start, end = 0, max(nums)

        while start < end :
            mid = start + (end - start)//2
            # print(f"mid :{mid}")
            count = self.get_count(nums, mid)
            # print(f"count : {count}")
            # if count == k:
            #     return diff
            if count < k:
                start = mid + 1
            else:
                end = mid

        return start

    def get_count(self, nums, target_diff):
        j = 1
        count = 0
        for i in range(len(nums)):
            while j < len(nums) and abs(nums[i] - nums[j]) <= target_diff:
                j  += 1
            count += (j - 1 -i )

        return count
