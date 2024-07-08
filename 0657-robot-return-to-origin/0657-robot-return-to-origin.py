class Solution:
    def judgeCircle(self, moves: str) -> bool:
        map = {"U" :999, "L": 1999, "D":-999 , "R":-1999}

        count = 0
        for move in moves:
            count += map[move]

        return count == 0

        