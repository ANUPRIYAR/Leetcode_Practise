class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        for x3, y3 in coordinates[2:]:
            if (y2 - y1)*(x3 -x2) != (y3 - y2)* (x2 - x1):
                return False

            x1, y1 = x2, y2
            x2, y2 = x3, y3
        return True
             


        