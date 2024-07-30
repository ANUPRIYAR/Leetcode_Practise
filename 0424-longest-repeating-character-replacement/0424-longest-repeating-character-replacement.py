class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        maxlen = 0
        hashmap = dict() 
        n = len(s)

        while end < n :
            char = s[end]
            hashmap[char] = hashmap.get(char, 0) + 1

            while (end - start + 1) - max(hashmap.values()) > k:
                start_char = s[start]
                hashmap[start_char] -= 1
                if hashmap[start_char] == 0:
                    del hashmap[start_char]

                start += 1


            # if (end - start + 1) - max(hashmap.values()) <=
            length = end - start + 1
            maxlen = max(maxlen, length)
            end += 1


        return maxlen



        