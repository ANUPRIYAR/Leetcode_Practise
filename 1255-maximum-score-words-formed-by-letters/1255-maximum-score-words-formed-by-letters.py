from collections import Counter
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], scores: List[int]) -> int:
        score_map = dict()
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for char, score in zip(alphabets, scores):
            score_map[char] = score

        letter_map = dict()
        for letter in letters:
            letter_map[letter] = letter_map.get(letter, 0) + 1

        def can_form_word(word, char_store):
            word_count = Counter(word)
            for char in word_count:
                if char_store.get(char, 0) < word_count[char]:
                    return False
            return True 

        
        def backtrack(index, letter_map, current_score):
            nonlocal maxscore
            if index == len(words):
                return current_score

            # skipping the current_word
            backtrack(index + 1, letter_map, current_score)

            word = words[index]
            if can_form_word(word, letter_map):
                word_score = 0
                for char in word:
                    letter_map[char] -= 1
                    word_score += score_map[char]

                backtrack(index + 1 , letter_map, current_score + word_score)
                maxscore = max(maxscore, current_score + word_score)

                # Retrack back
                for char in word:
                    letter_map[char] += 1
                
        
        maxscore = 0
        backtrack(0, letter_map, 0)
        return maxscore
                    
                    
                


            
        


        