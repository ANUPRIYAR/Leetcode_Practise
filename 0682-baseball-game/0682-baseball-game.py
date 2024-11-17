class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "C" and stack:
                stack.pop()
            elif op == "D" and stack:
                stack.append(2*stack[-1])
            elif op == "+" and len(stack) > 1:
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))

        return sum(stack)



        