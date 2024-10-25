class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        count = 0
        start = 0
        length = len(s)
        freq_map = dict()

        for end in range(length):
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1

            while freq_map[s[end]] >= k:
                count += length - end
                freq_map[s[start]] -= 1
                start += 1

        return count


        

    
    
            
        