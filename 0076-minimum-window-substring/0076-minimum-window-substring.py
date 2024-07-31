import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, end = 0, 0
        n = len(s) 
        freq_t, freqs = dict(), dict()
        min_window = math.inf
        minsubstr = ""

        for char in t:
            freq_t[char]  = freq_t.get(char, 0) + 1


        while end < n:
            char = s[end]
            freqs[char] = freqs.get(char, 0) + 1


            while self.match(freqs, freq_t):
                substring = s[start: end + 1]
                length = end - start + 1
                if length < min_window:
                    min_window = length
                    minsubstr = substring


                start_char = s[start]
                freqs[start_char] -= 1
                if freqs[start_char] == 0:
                    del freqs[start_char]

                start += 1

            end += 1
        return minsubstr


            




            







    def match(self, maps, mapt):
        for char in mapt:
            if maps.get(char, 0) < mapt[char]:
                return False
        return True 




        