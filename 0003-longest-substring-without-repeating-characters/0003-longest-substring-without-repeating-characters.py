class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = dict()
        left, right= 0, 0 
        maxlen = 0

        while right < len(s):
            char = s[right]
            
            if char in hashmap and (left <= hashmap.get(char, -1) <= right):
                left = hashmap[char] + 1

            hashmap[char] = right
            length = right - left + 1
            maxlen = max(maxlen, length)
            right += 1

        return maxlen


                


        


        