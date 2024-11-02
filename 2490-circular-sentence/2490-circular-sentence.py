class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentences = sentence.split(' ')

        if len(sentences) == 1:
            if ord(sentences[0][-1]) != ord(sentences[0][0]):
                return False

        n = len(sentences)
        for i in range(2*n):
            print(i%n,  (i+1)%n)
            if ord(sentences[i % n][-1]) != ord(sentences[(i+1) % n][0]):
                return False

        return True

        
        