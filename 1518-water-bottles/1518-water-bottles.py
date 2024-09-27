class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles

        while numBottles >=  numExchange:
            bottles =  numBottles//numExchange
            drank += bottles
            numBottles = (numBottles % numExchange) + bottles

        return drank
        