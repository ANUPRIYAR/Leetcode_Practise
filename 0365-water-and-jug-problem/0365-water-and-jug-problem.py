class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        visited = set()

        def dfs(a, b):
            
            if a + b == target:
                return True 

            if a < 0 or a > x or b < 0 or b > y or (a, b) in visited:
                return False

            visited.add((a, b))
            
            if dfs(x, b):
                return True 
            if dfs(a, y):
                return True 
            if dfs(0, b):
                return True 
            if dfs(a, 0):
                return True

            transfer_x_to_y = min(a, y - b)
            if dfs(a - transfer_x_to_y, b + transfer_x_to_y):
                return True 

            transfer_y_to_x = min(b, x - a)
            if dfs(a + transfer_y_to_x, b - transfer_y_to_x ):
                return True 

            return False

        return dfs(x, y)






        
        