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





        # max_val = 1000
        # count = [0] * (2*max_val + 1)


        # # Get Count
        # for num in nums:
        #     count[num + max_val] += 1

        # # Calculate Cumulative Freqeuency
        # for i in range(1,len(count)):
        #     count[i] += count[i-1]


        # total_sum = 0
        # add = True

        # # Traverse the count array
        # # while j < len(output):
        # #     while count[i] > 0:
        # #         if add:
        # #             total_sum += i -max_value
        # #         add = not add
        # #         count[i] -= 1



        # output = [0]* len(nums)
        # for num in nums:
        #     output[count[num] - 1] = num
        #     count[num] -= 1

        # # Create Pairs and take minimum
        # # sum = 0
        # # i, j = 0, 1
        # # while j < len(output):
        # #     sum += min(output[i], output[j])
        # #     i += 2
        # #     j += 2


        # # return sum







        