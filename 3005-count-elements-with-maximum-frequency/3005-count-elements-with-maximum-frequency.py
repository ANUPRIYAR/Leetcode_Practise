class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_map = dict()
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        max_freq = max(list(freq_map.values()))
        
        
        freq_map = dict(sorted(freq_map.items(), key = lambda x:x[1],  reverse=True))

        total_freq = 0
        for key, value in freq_map.items():
            print(value)
            if value == int(max_freq):
                total_freq += value
            else:
                break

        return total_freq
