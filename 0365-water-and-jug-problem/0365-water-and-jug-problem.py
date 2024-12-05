class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        visited = set()   # To keep track of visited states
        
        def dfs(a: int, b: int):
            if (a,b) in visited or a > x or b > y or a < 0 or b < 0:
                return False
            
            visited.add((a,b))
            
            # Check if we've reached our target volume
            if a + b == target:
                return True
            
            # Explore all possible operations
            
            # Fill jug x completely
            if dfs(x, b): 
                return True
            
            # Fill jug y completely
            if dfs(a, y): 
                return True
            
            # Empty jug x completely
            if dfs(0, b): 
                return True
            
            # Empty jug y completely
            if dfs(a ,0): 
                return True
            
            # Pour water from jug x to jug y until one is full or one is empty.
            transfer_to_y = min(a ,y - b)
            if dfs(a - transfer_to_y ,b + transfer_to_y):
                return True
            
             # Pour water from jug y to jug x until one is full or one is empty.
            transfer_to_x = min(b ,x - a)
            if dfs(a + transfer_to_x ,b - transfer_to_x):
                return True

            return False
        
        return dfs(0 ,0)