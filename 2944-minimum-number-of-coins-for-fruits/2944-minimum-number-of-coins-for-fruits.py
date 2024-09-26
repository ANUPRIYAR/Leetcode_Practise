from collections import deque

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        minqueue = deque()
        minqueue.append(n)
        prices = prices + [0]


        for i in range(n-1, -1, -1):
            max_index = min(n, 2*i + 2)

            while minqueue and minqueue[0] > max_index:
                minqueue.popleft()

            prices[i] += prices[minqueue[0]]

            while minqueue and prices[minqueue[-1]] > prices[i]:
                minqueue.pop()
            minqueue.append(i)

        return prices[0]



            




        