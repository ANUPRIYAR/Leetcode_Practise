class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        start = 0
        freq = dict()
        count = 0
        n = len(s)
        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1

            while freq[s[end]] >= k:
                count += n - end
                freq[s[start]] -= 1
                start += 1

        return count

        