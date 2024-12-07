class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        string = ""
        prev_sp = 0

        for sp in spaces:
            string += s[prev_sp:sp] + " "
            prev_sp = sp

        string += s[prev_sp:]
        return string

        