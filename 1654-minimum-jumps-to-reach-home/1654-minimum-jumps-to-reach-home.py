class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        F = set(forbidden)
        visited = set()
        @lru_cache(None)
        def dfs(i,isPrevBack):
            if (i,isPrevBack) in visited: return math.inf
            else: visited.add((i,isPrevBack))
            if i == x: return 0
            if i in F or i > 6000: return math.inf
            if isPrevBack or i - b <= 0: return 1 + dfs(i + a, False)
            return 1 + min(dfs(i + a, False), dfs(i - b, True))
        ans = dfs(0,False)
        return ans if ans < math.inf else -1