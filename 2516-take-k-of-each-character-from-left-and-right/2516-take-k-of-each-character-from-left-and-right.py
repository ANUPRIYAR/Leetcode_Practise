class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # if k == 0:
        #     return 0

        n = len(s)
        min_minutes = float('inf')
        offset = ord("a")

        count = [0]*3
        for char in s:
            count[ord(char) - ord("a")] += 1

        if min(count) < k:
            return -1
            
        start = 0
        for end in range(len(s)):
            count[ord(s[end]) - offset] -= 1

            while min(count) < k:
                count[ord(s[start]) - offset] += 1
                start += 1

            if min(count) >= k:
                min_minutes = min(min_minutes, n - (end - start + 1))


        return min_minutes





        

        
            