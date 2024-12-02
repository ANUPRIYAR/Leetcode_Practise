class Solution:
    def __init__(self):
        self.perfect_squares = []
        self.minlength = float('inf')

    def numSquares(self, n: int) -> int:
        self.perfect_squares = self.create_squares(n)
        def helper(n, memo):
            if n in memo:
                return memo[n]
            if n == 0:
                return []
            if n < 0:
                return None

            smallest_combination = None
            for square in self.perfect_squares:
                rem = n - square
                result = helper(rem, memo)
                if result is not None:
                    combination =  result + [square]
                    if smallest_combination is None or len(combination) < len(smallest_combination):
                        smallest_combination = combination
                         
            memo[n] = smallest_combination
            return memo[n]

        output = helper(n, {})
        
        return len(output) if output is not None else -1

    def create_squares(self, n):
        self.perfect_squares = [i*i for i in range(1, int(sqrt(n)) + 1)]
        return self.perfect_squares 






            

        


        
        