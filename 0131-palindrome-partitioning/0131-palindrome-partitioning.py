class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.find(s, 0, result, [])
        return result

    def find(self, s, start, result, current):
        if start == len(s):
            result.append(current[:])
            return

        for i in range(start , len(s)):
            if self.is_palindrome(s, start, i):
                current.append(s[start : i + 1])
                self.find(s, i + 1, result, current)
                current.pop()               



    def is_palindrome(self, s, start , end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True