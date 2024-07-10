class Solution:
    def validStrings(self, n: int) -> List[str]:
        def backtrack(string):
            if len(string) == n:
                result.append(string)
                return

            backtrack(string + '1')   # Always safe to add 1
            if not string or string[-1] == '1':
                backtrack(string + '0')   # Add 0 only if above condition satisfied
                

        result = []
        backtrack("")
        return result

            
                
            