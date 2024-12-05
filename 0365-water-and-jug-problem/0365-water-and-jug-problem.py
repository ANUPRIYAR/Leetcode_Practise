class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        visited = set()   # To keep track of visited states
        
        def dfs(a: int, b: int):
            if (a,b) in visited or a > x or b > y or a < 0 or b < 0:
                return False
            
            visited.add((a,b))
            
            if a + b == target:
                return True

            if dfs(x,b):
                return True

            if dfs(a, y):
                return True

            if dfs(0, b):
                return True

            if dfs(a, 0):
                return True

            transfer_x_to_y = min(a, y-b)
            if dfs(a - transfer_x_to_y, b + transfer_x_to_y):
                return True

            transfer_y_to_x = min(b, x - a)
            if dfs(a + transfer_y_to_x, b - transfer_y_to_x  ):
                return True
            return False

        return dfs(0, 0)
 

            