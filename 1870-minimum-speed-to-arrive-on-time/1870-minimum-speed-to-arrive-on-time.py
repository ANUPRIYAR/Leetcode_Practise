import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def can_reach(x):
            total_hours = 0
            for d in dist[:-1]:
                total_hours += math.ceil(d/x)
            
            total_hours += dist[-1]/x
            return total_hours <= hour
        
        left = 1
        right = 10**10
        
        while left <= right:
            mid = left + (right - left)//2

            if can_reach(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left if left <= 10**10 else -1

            