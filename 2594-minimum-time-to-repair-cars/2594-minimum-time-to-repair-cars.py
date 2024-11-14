class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        counter = Counter(ranks)
        def canrepair(time):
            toberepaired = cars

            for rank , freq in counter.items():
                toberepaired -= math.floor((time/rank)**0.5) * freq
                if toberepaired <= 0:
                    return True

            return False

        left  = min(ranks)
        right = max(ranks)* (cars**2)

        while left <= right:
            mid = (left + right)//2

            if canrepair(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left



        