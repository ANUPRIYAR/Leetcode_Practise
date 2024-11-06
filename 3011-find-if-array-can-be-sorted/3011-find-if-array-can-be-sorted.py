class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n  = len(nums)
        if n < 2:
            return True
        def count_setbits(n):
            count = 0
            while n > 0:
                count += n & 1 # n%2
                n >>= 1  # n//2
            return count

        start = 0
        for end in range(1,n):
            if count_setbits(nums[end - 1]) != count_setbits(nums[end]):
                max_element = max(nums[start:end])
                print(f"maxelement : {max_element}")
                j = end
                while j < n-1 and count_setbits(nums[j]) == count_setbits(nums[j + 1]):
                    j += 1
                min_element = min(nums[end:j +1 ])
                print(f"minelement : {min_element}")
                if max_element > min_element:
                    return False

                start = end

        return True
                
                 
