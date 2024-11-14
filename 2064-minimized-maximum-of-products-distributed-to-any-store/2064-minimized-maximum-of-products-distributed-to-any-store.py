class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def can_distribute(x):
            covered_stores = 0
            for quantity in quantities:
                covered_stores += math.ceil(quantity/x)
            
            return covered_stores <= n

        left = 1
        right = max(quantities)
        result = 0

        while left <= right:
            mid = left + (right-left)//2
            if can_distribute(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

            

        