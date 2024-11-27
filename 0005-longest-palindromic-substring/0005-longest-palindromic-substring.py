class Solution:
    def __init__(self):
        self.maxstring = ''

    def longestPalindrome(self, s: str) -> str:
        n  = len(s)
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(n):
            dp[i][i] = True
        
        maxlength = 0
        self.maxstring = s[0]
        for start in range(n-1, -1, -1):
            for end in range(start + 1, n):
                if s[start] == s[end]:
                    if end - start ==1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if end- start +1 > maxlength:
                            maxlength = end- start +1
                            self.maxstring = s[start: end + 1]

        return self.maxstring 