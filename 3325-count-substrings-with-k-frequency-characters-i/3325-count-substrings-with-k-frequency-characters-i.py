class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        start = 0
        count = 0
        freq = dict()
        length = len(s)

        for end in range(length):
            char = s[end]
            freq[char] = freq.get(char, 0) + 1

            while freq[char] >= k:
                count += length - end
                freq[s[start]] -= 1
                start  += 1


        return count

                
        