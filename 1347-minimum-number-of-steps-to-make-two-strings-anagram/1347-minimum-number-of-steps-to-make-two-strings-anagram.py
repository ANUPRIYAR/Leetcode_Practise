class Solution:
    def minSteps(self, s: str, t: str) -> int:
        diff_map= dict()
        for char_s, char_t in zip(s, t):
            diff_map[char_t] = diff_map.get(char_t, 0) + 1
            diff_map[char_s] = diff_map.get(char_s, 0) - 1

        steps = 0
        for k, v in diff_map.items():
            if v > 0 :
                steps += v

        return steps



        