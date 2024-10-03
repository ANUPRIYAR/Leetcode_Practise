from collections import Counter
import heapq
from heapq import heappush , heappop 
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        maxheap = []
        for char, freq in count.items():
            heappush(maxheap, (-freq, char))

        result = ''
        while maxheap:
            freq, char = heappop(maxheap)
            result += char * (-freq)
        return result


        


        