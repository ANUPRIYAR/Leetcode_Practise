class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen_index = {'a': -1, 'b': -1, 'c' : -1}

        answer = 0

        for index, char in enumerate(s):
            last_seen_index[char] = index
            answer += min(last_seen_index.values()) + 1

        return answer
        