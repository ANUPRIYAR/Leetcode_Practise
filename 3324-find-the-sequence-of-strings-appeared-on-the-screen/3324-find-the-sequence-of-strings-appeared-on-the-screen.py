class Solution:
    def stringSequence(self, target: str) -> List[str]:
        result = []
        string = ["a"]
        result.append(''.join(string))
        for i in range(len(target)):
            while target[i] != string[i]:
                string[i] = chr(ord(string[i]) + 1)
                joined = ''.join(string)
                result.append(joined)
            if len(target) != len(string):
                string.append("a")
                result.append(''.join(string))
            else:
                break

        return result

        
        
        