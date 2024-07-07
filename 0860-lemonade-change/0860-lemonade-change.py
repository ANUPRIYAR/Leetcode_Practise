class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_counter = dict()
        bill_counter[5] = bill_counter[10] = bill_counter[20] = 0

        for  bill in bills:
            
            if bill != 5:
                change = bill - 5
                if change > 0:
                    if bill_counter.get(change, 0) > 0:
                        bill_counter[change] -= 1
                    elif change == 5:
                        return False
                    elif change == 15:
                        if bill_counter[10] > 0 and bill_counter[5] > 0:
                            bill_counter[10] -= 1
                            bill_counter[5] -= 1
                        elif bill_counter[5] >= 3:
                            bill_counter[5] -= 3
                        else:
                            return False
            bill_counter[bill] += 1

        return True






                


        