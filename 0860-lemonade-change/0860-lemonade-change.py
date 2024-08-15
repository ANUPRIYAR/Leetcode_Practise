class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens, twenties = 0, 0, 0
        cost = 5
        balance = 0

        for bill in bills:
            balance = bill - cost
            if balance == 15:
                # if tens > 0:
                #     tens -= 1
                # else:
                #     fives -= 2
                tens -= 1 if tens > 0 else(fives := fives - 2)
                fives -= 1 
            elif balance == 5:
                fives -= 1
            if fives < 0:
                return False
            if bill == 5:
                fives += 1
            if bill == 10:
                tens += 1
            if bill == 20:
                twenties += 1

        return True