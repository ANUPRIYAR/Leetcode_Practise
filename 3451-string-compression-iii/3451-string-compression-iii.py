from collections import deque
class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        stack = deque()
        stack.append([word[0] , 1])
        comp = ""
        i = 1
        while stack and i < n:
            if stack[-1][0] == word[i]:
                _, count = stack.pop()
                count += 1
                stack.append([word[i], count])       
            else:
                stack.append([word[i], 1])
            i += 1


        # print(stack)

        while stack:
            char, count = stack.popleft()
            while count > 9:
                comp += f"9{char}"
                count -= 9
            if count > 0:
                comp += f"{count}{char}"
        
        return comp
            
        
       