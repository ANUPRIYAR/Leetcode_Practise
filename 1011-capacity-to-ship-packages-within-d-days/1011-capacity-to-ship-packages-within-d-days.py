class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def can_ship(daily_limit):
            # for weight in weights:
            #     total_days += math.ceil(weight/x)
            total_weights= 0
            d = 1
            for weight in weights:
                if total_weights + weight > daily_limit:
                    d += 1
                    total_weights = weight
                else:
                    total_weights += weight
            
            return d <= days

        left = max(weights)
        right = sum(weights) * 500
        result = None
        while left <= right:
            mid = left + (right - left)//2

            if can_ship(mid):
                result = mid
                right = mid -1
            else:
                left = mid + 1

        return left


        