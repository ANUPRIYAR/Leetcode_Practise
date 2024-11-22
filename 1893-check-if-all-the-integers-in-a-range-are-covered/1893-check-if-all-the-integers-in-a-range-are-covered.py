class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        count = [0]* 52
        for start, end in ranges:
            count[start] += 1
            count[end + 1] -= 1


        cursum  = 0
        for i in range(right + 2):
            cursum += count[i]
            
            if i >=left and  i <= right and cursum <= 0:
                return False

        return True 





        