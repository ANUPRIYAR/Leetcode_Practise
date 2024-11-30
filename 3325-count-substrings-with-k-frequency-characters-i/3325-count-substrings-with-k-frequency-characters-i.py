class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        start = 0
        count = 0
        length = len(s)
        freq = dict()

        for end in range(length):
            freq[s[end]] = freq.get(s[end], 0) + 1

            while freq[s[end]] >= k:
                count += length - end
                freq[s[start]] -= 1
                start += 1

        return count