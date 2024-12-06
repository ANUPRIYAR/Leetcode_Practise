class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        prefix_sum = []
        array = []
        cumsum = 0
        j = 0
        for i in range(1,n + 1):
            if i not in banned and i <= maxSum:
                array.append(i)
                cumsum += array[j]
                if cumsum > maxSum:
                    return j 
                elif cumsum == maxSum:
                    return j + 1
                j += 1
        return len(array)