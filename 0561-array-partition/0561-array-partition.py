class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)

        count = [0]*(max_val - min_val + 1)

        # take count
        for num in nums:
            count[num- min_val] += 1

        # cumulative sum
        for i in range(1, len(count)):
            count[i] += count[i-1]

        # Create output array
        output = [0]* len(nums)
        for num in nums:
            output[count[num- min_val] - 1] = num
            count[num - min_val] -= 1
        

        # Get sum of pairs
        i, j = 0, 1
        sum_ = 0
        while j < len(nums):
            sum_ += min(output[i], output[j])
            i += 2
            j += 2
        return sum_