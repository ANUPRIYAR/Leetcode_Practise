class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        freq = {"a" : 0 , "b" : 0, "c":0}
        n = len(s)
        min_minutes = float('inf')

        
        count = [0]*3
        for char in s:
            count[ord(char) - ord("a")] += 1

        for c in count:
            if c < k:
                return - 1
            
        start = 0
        for end in range(len(s)):
            freq[s[end]] += 1

            while count[0]- freq["a"] < k or count[1] - freq["b"] < k or count[2] - freq["c"] < k:
                freq[s[start]] -= 1
                start += 1

            if count[0]- freq["a"] >= k and count[1] - freq["b"] >= k and count[2] - freq["c"] >= k:
                min_minutes = min(min_minutes, n - (end - start + 1))


        return min_minutes





        

        
            