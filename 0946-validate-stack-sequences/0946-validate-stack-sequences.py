class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        n = len(pushed)
        stack = []
        ele = 9999
        while i < n or j < n:
            if popped[j] not in stack:
                stack.append(pushed[i])
                i += 1
                
            else:
                if len(stack) > 0:
                    ele = stack.pop()
                if (ele == popped[j]):
                    j += 1
                else:
                    return False

        if i == n and j == n :
            return True

        
        

  
        

        