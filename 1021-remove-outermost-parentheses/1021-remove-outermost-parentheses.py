class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        outerstack = []
        innerstack = []

        bracket = 0
        for char in s:
            if char == '(':
                if not outerstack:
                    outerstack.append(char)
                else:
                    innerstack.append(char)
                    bracket += 1
            elif char == ')':
                if bracket > 0:
                    innerstack.append(char)
                    bracket -= 1
                elif outerstack and bracket == 0:
                    outerstack.pop()

        return ''.join(innerstack)



                    
                



        