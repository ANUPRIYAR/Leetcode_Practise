class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = { ')' : '(',
                         '}': '{',
                        ']': '[' }

        if len(s) % 2 !=0:
            return False

        stack = []
        for char in s:
            # Add closing bracket encountered, it should have a matching opening bracket in stack
            if char in bracket_map.keys():
                if not stack or bracket_map[char] != stack.pop():
                    return False
               
            else:
                stack.append(char)
        
        return len(stack) == 0

        