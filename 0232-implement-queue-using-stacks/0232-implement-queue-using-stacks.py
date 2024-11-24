class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)

        

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        popped = self.stack2.pop()
        self.stack1 = self.stack2[::-1]
        self.stack2 = []
        return popped

    
    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        top_item = self.stack2.pop()
        self.stack2.append(top_item)
        self.stack1 = self.stack2[::-1]
        self.stack2 = []
        return top_item
        

    def empty(self) -> bool:
        return len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()