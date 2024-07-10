class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def backtracking(start, seen, current):
            nonlocal max_count
            if start == len(s):
                max_count = max(max_count, len(current))
                return 

            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if substr not in seen:
                    seen.add(substr)
                    current.append(substr)
                    backtracking(end, seen, current)
                    current.pop()
                    seen.remove(substr)

        max_count = 0
        backtracking(0, set(), [])
        return max_count




        