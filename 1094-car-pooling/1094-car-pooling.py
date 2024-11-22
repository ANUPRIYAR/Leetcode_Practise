class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        count = [0]* 1002
        
        trips.sort(key = lambda x:(x[1], x[2]))
        for pass_count, start, end in trips:
            count[start] += pass_count
            count[end] -= pass_count


        cursum = 0
        for i in range(len(count)):
            cursum += count[i]

            if cursum > capacity:
                return False
        return True

        