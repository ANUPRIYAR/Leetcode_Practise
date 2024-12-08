class Solution:
    def climbStairs(self, n: int) -> int:
       
        def helper(n , memo):
            if n in memo:
                return memo[n]
            if n==0:
                return 1

            if n < 0:
                return 0

            memo[n] =  helper(n-1, memo) + helper(n-2, memo) 
            return memo[n]

        return helper(n, {})
        
        