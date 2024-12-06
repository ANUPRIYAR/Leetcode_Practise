class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        self.cache = {}
        visited = set()
        forbit = set(forbidden)
        
        # Determine max limit based on forbidden positions
        max_limit = 2000 + 2 * b
        for num in forbidden:
            max_limit = max(max_limit, num + 2 * b)

        val = self.helper(0, x, a, b, forbit, visited, 0, max_limit)
        
        return -1 if val == float('inf') else val

    def helper(self, idx, x, a, b, forbit, visited, dir_last_jump, max_limit):
        # Check if we have already computed this state
        if (idx, dir_last_jump) in self.cache:
            return self.cache[(idx, dir_last_jump)]
        
        # Base cases
        if idx == x:
            return 0
        if idx < 0 or idx > max_limit:
            return float('inf')
        
        visited.add(idx)
        
        min_jumps = float('inf')

		# Try jump forward
        if idx + a < max_limit and (idx + a) not in forbit and (idx + a) not in visited:
            step = self.helper(idx + a , x ,a ,b ,forbit ,visited ,0 ,max_limit)
            if step != float('inf'):
                min_jumps = min(min_jumps ,step + 1)

		# Try jump backward only if last jump was not backward
        if idx - b >= 0 and (idx - b) not in forbit and (idx - b) not in visited and dir_last_jump != 1:
            step = self.helper(idx - b ,x ,a ,b ,forbit ,visited ,1,max_limit)
            if step != float('inf'):
                min_jumps = min(min_jumps ,step + 1)

        # Backtrack: remove current index from visited set
        visited.remove(idx)

        # Cache the result before returning it
        self.cache[(idx,dir_last_jump)] = min_jumps

        return min_jumps
