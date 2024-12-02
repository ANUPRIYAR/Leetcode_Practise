class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def helper(coins, amount, memo):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return []

            if amount < 0:
                return None

            smallest_combination = None
            for coin in coins:
                rem = amount - coin
                result = helper(coins, rem, memo)

                if result  is not None:
                    combination = result + [coin]

                    if smallest_combination is None or len(combination) < len(smallest_combination):
                        smallest_combination = combination
            memo[amount] = smallest_combination
            return memo[amount]


        smallest_combination = helper(coins, amount, {})
        return len(smallest_combination) if smallest_combination is not None else -1 







        
        