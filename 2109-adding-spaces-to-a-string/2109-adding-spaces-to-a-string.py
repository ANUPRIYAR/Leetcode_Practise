class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s_list = list(s)
        count = 0
        string = ""
        prev_sp = 0
        for sp_idx in spaces:
            string += s[prev_sp:sp_idx] + " " 
            prev_sp = sp_idx
            
        string += s[sp_idx:]
        return string