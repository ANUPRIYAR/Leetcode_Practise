class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_map = dict()

        for word in words:
            freq_map[word] = freq_map.get(word, 0) + 1

        freq_map = dict(sorted(freq_map.items(), key = lambda x : (-x[1],x[0]) ))

        keys = list(freq_map.keys())

        return keys[:k]
        