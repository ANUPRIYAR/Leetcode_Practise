class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = start^goal
        count = 0
        while result > 0:
            result &= result - 1
            count += 1
        return count

        