class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(daily_limit):
            days_reqd = 1
            current = 0
            for weight in weights:
                if current + weight > daily_limit:
                    days_reqd += 1
                    current = weight
                else:
                    current += weight

            return days_reqd <= days

        left = max(weights)
        right = sum(weights)*500

        while left <= right:
            mid = left + (right- left)//2
            if can_ship(mid):
                right = mid -1 
            else:
                left = mid + 1

        return left
