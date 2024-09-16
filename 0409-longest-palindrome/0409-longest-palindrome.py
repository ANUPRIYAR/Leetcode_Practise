class Solution:
    def longestPalindrome(self, s: str) -> int:
        charmap = dict()

        for char in s:
            charmap[char] = charmap.get(char, 0) + 1
        
        charmap = dict(sorted(charmap.items(), key = lambda x: x[1], reverse=True))

        pal_count = 0
        odd = False
        for key, value in charmap.items():
            if value % 2 == 0:
                pal_count += value
            else:
                odd = True
                pal_count += (value - 1)

        return pal_count + 1 if odd else pal_count
        