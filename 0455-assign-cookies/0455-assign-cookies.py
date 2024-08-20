class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g_idx = s_idx = 0
        s.sort()
        g.sort()
        n = len(g)
        len_s = len(s)
        count = 0
        while g_idx < n and s_idx < len_s:
            if g[g_idx] <= s[s_idx]:
                count += 1
                g_idx += 1
            s_idx += 1

        return count
            



            

        