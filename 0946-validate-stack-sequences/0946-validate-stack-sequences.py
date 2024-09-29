class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        n = len(pushed)
        stack = []
        ele = 999999
        while i < n or j < n:
            if popped[j] not in stack:
                stack.append(pushed[i])
                # print(stack)
                i += 1
                # print(f"i : {i} ")
                
            else:
                if len(stack) > 0:
                    ele = stack.pop()
                # print(f"popped : {ele}")
                if (ele == popped[j]):
                    j += 1
                    # print(j)
                else:
                    return False

        if i == n and j  == n :
            return True

        
        

  
        

        