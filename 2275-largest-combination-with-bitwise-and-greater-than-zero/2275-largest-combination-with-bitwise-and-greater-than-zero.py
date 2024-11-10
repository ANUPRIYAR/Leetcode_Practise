class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_count = [0] * 32

        max_freq = 0
        for num in candidates:
            for i in range(32):
                x = 1 << i
                if num &  x != 0:
                    bit_count[i] += 1
                    if bit_count[i] > max_freq:
                        max_freq = bit_count[i]

        return max_freq
        
    

        