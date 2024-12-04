class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        offset = ord('a')
        i, j = 0, 0

        while i < len(str1)  and j < len(str2):

            if str1[i] == str2[j] or (ord(str1[i]) - offset + 1)% 26 == ord(str2[j]) - offset:
                i += 1
                j += 1
            else:
                i += 1

        return j == len(str2)