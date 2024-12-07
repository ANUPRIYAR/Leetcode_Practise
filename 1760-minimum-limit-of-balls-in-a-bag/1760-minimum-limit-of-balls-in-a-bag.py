class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def helper(bagsize):
            idealbagcount = (sum(nums)//bagsize)
            operations = idealbagcount - len(nums)
            # operations = 0
            # for item_count in nums:
            #     if item_count > bagsize:
            #         operations += 1
            #         cursize = item_count - idealbagcount
            #         while cursize 
            #         nums.append(item_count - idealbagcount)

            return operations <= maxOperations

        left = 1
        right = max(nums) 
        while left < right:
            mid = left + (right - left)//2
            ans = None
            if helper(mid):
                ans = mid
                right = mid 
            else:
                left = mid + 1

        return right
                    

        