class Solution:
    def canCross(self, stones: List[int]) -> bool:
        k = 1 # units
        if stones[1] != 1:
            return False

        def helper(position, k, memo):
            if (position, k) in memo:
                return memo[(position, k)]

            if position == len(stones) - 1:
                return True 

            for jump in (k-1, k, k+1):
                if jump > 0:
                    if stones[position] + jump in stones:
                        next_index = stones.index(stones[position] + jump)
                        if helper(next_index, jump, memo):
                            memo[(position, k)] = True 
                            return True


            memo[(position, k)] = False  
            return False

        return helper(1, 1, {})
            


