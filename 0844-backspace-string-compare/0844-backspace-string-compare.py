class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def create_stack(s):
            stack = []
            count = 0
            for char in s:
                if char == '#':
                    count += 1
                elif count > 0:
                    while stack and count > 0:
                        stack.pop()
                        count -= 1
                    count = 0
                if char != '#':
                    stack.append(char)
                print(stack)
                print(count)

            while stack and count > 0:
                stack.pop()
                count -= 1
            return stack 

        stack1= create_stack(s)
        stack2 = create_stack(t)
        print(stack1, stack2)

        return stack1 == stack2

        
        