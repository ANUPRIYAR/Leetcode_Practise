class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count_vowels = 0
        
        for char in s:
            if char in vowels:
                count_vowels += 1
                
        if count_vowels == 0:
            return False
        else:
            return True
                
        
            
        