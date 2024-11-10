class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # start with x, coz thats the smallest num with alll bits same as x
        answer = x

        # to find nth output, we can iterate n times
        while n > 1:
            # taking next greater number and oring it with x , to set all bits as x
            answer = (answer + 1) | x
            n -= 1

        return answer
        
    