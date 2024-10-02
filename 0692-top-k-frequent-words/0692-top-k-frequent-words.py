from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        bucket = [[] for i in range(len(words))]

        for char, freq in count.items():
            bucket[freq].append(char)
            
        for i in range(len(bucket)):
            bucket[i].sort()

        res = []
        # Iterate from reverse to get most frequent bucket first
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res



    