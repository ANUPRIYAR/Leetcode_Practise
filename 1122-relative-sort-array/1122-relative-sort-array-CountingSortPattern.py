class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_val  = max(arr1)
        count = [0] * (max_val + 1)

        # Get the count of elements in arr1
        for num in arr1:
            count[num] += 1

        
        # add num to result in the realtive ordering of elemnts in arr2
        result = []
        for num in arr2:
            while count[num] > 0:
                result.append(num)
                count[num] -= 1


        # Add the rest of the elemnts in arr1 to result in increasing order
        for i in range(len(count)):
            while count[i] > 0:
                result.append(i)
                count[i] -= 1

        return result
