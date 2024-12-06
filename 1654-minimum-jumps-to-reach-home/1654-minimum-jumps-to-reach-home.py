class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden_set = set(forbidden)
        max_position = max(x + a + b, 2000)  # Set an upper limit for exploration
        memo = {}
        visited = set()

        def dfs(position, jumps, last_jump):
            # Base case: if we've reached home
            if position == x:
                return jumps

            visited.add((position, last_jump))
            
            # If out of bounds or forbidden
            if position < 0 or position > max_position or position in forbidden_set and (position, last_jump) not in visited:
                return float('inf')
            
            # Memoization check
            if (position, last_jump) in memo:
                return memo[(position, last_jump)]
            
            # Explore forward jump
            forward_jumps = dfs(position + a, jumps + 1, 'F')
            
            # Explore backward jump only if last was not backward
            backward_jumps = float('inf')
            if last_jump != 'B':
                backward_jumps = dfs(position - b, jumps + 1, 'B')

            # Store result in memoization dictionary
            result = min(forward_jumps, backward_jumps)
            memo[(position,last_jump)] = result
            
            return result

        res = dfs(0, 0,'F')  # Start from position 0 with 0 jumps and no previous direction
        
        return res if res != float('inf') else -1