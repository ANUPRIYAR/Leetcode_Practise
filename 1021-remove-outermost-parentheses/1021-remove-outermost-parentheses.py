class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        outerstack = []
        innerstack = []

        flag = 0
        for char in s:
            if char == "(":
                if not outerstack:
                    outerstack.append(char)
                else:
                    innerstack.append(char)
                    flag += 1
            else:
                if flag:
                    innerstack.append(char)
                    flag -= 1
                else:
                    outerstack.pop()

        return ''.join(innerstack)

            
           