from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        buckets = [[] for i in range(len(s) + 1)]

        for char, freq in count.items():
            buckets[freq].append(char)

        result = ''
        for i in range(len(buckets)-1, 0, -1):
            for char in buckets[i]:
                result += char * i
        
        return result
        


        