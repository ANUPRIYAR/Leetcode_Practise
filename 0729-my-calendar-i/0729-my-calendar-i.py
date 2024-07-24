from sortedcontainers import SortedList

# class Node:
#     def __init__(self, left, right, start, end):
#         self.calender = SortedList()

class MyCalendar:

    def __init__(self):
         self.calender = SortedList()
        

    def book(self, start: int, end: int) -> bool:
        idx = self.calender.bisect_right((start, end))
        if (idx > 0 and self.calender[idx -1][1] > start) or (idx < len(self.calender) and self.calender[idx][0] < end):
            return False
        self.calender.add((start, end))
        return True 

       
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)