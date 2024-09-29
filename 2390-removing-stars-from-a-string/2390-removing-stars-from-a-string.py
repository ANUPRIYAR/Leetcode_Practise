class Solution:
    def removeStars(self, s: str) -> str:
        remove = 0
        res = []
        for i in range(len(s) -1, -1, -1):        
            if s[i] == '*':
                 remove += 1
            elif remove > 0:
                remove -= 1
                continue
            else:
                res.append(s[i])

        return ''.join(res[::-1])
               
            


            
        