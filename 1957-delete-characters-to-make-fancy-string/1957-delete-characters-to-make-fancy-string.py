class Solution:
    def makeFancyString(self, s: str) -> str:
        fancy_string = ""
        start, end = 0, 1
        n = len(s)

        if len(s)<= 2:
            return s

        while end < n:
            while  end < n and s[start] == s[end]:
                end += 1

            if end - start >= 3:
                fancy_string += s[start]*2
            else:
                fancy_string += s[start:end]
            
            start = end
            end += 1

        if s[-1] != s[-2]:
            fancy_string += s[-1]
        
        return fancy_string

        

        