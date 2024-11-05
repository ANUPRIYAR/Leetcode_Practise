from collections import deque
class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        count = 1
        i = 1
        stack = deque()
        stack.append([s[0], 1])

        i = 1
        while stack and i < len(s):
            char, count = stack.pop()
            if count % 2 != 0 and  char != s[i]:
                changes += 1
                stack.append([char, count + 1])
                count = 0
            else:
                stack.append([s[i], count + 1])
            i += 1

        return changes


        
       