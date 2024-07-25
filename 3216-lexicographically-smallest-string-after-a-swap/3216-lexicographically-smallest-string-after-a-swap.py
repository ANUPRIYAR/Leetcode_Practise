class Solution:
    def getSmallestString(self, s: str) -> str:
        
        digits = s
        digits = [int(dig) for dig in digits]
        
        for i in range(len(digits)-1):
            if digits[i]%2 == digits[i+1]%2:
                if digits[i] > digits[i+1]:
                    digits[i], digits[i+1] = digits[i+1], digits[i]
                    break
                    
                    
        return ''.join(list(map(str, digits)))
        