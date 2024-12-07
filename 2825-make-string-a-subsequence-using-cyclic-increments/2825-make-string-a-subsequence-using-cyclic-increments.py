class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        char_map = dict()
        for ord_i in range(ord('a'), ord('z')):
            char_map[chr(ord_i)] = chr(ord_i + 1)
        char_map['z'] = 'a'
        print(char_map)

        i, j = 0, 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j] or char_map[str1[i]] == str2[j]:
                i += 1
                j += 1
            else:
                i += 1

        return j == len(str2)
        