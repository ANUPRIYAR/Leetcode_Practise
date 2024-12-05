from math import gcd
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # Check if target is greater than the total capacity
        if target > x + y:
            return False
        
        # Check if target is achievable with gcd condition
        if target % gcd(x, y) != 0:
            return False
        
        # BFS initialization
        visited = set()
        queue = deque([(0, 0)])  # Start with both jugs empty
        
        while queue:
            a, b = queue.popleft()
            
            # Check if we've reached our target volume
            if a + b == target:
                return True
            
            # If already visited this state, skip it
            if (a, b) in visited:
                continue
            
            visited.add((a, b))
            
            # Possible operations
            
            # Fill jug x completely
            queue.append((x, b))
            
            # Fill jug y completely
            queue.append((a, y))
            
            # Empty jug x completely
            queue.append((0, b))
            
            # Empty jug y completely
            queue.append((a ,0))
            
            # Pour water from jug x to jug y until one is full or one is empty.
            transfer_to_y = min(a ,y - b)
            queue.append((a - transfer_to_y ,b + transfer_to_y))
            
             # Pour water from jug y to jug x until one is full or one is empty.
            transfer_to_x = min(b ,x - a)
            queue.append((a + transfer_to_x ,b - transfer_to_x))

        return False