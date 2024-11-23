class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])

        prev_end = pairs[0][1]
        chain_length = 1
        for start, end in pairs[1:]:
            if prev_end < start :
                chain_length += 1
                prev_end = end

        return chain_length

        