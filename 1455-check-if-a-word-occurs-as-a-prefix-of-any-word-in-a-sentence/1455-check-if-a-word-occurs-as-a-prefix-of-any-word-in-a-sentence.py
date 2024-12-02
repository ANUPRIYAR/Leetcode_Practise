class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        words = sentence.split(' ')
        j = None
        for i, word in enumerate(words):
            if word[0] == searchWord[0]:
                wordlength = len(word)
                j = 0
                while j  < min(wordlength, len(searchWord)) and word[j] == searchWord[j]:
                    j += 1

                if j <= wordlength and j == len(searchWord):
                    return i + 1

        return -1
            


        