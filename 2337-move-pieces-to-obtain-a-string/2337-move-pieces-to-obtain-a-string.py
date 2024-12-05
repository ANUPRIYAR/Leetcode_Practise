class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # sl, tl = 0.
        # sr = tr = len(start) - 1 
        start_freq = Counter(start)
        target_freq = Counter(target)
        if start_freq != target_freq:
            return False

        start += '@'
        target += '@'
        
        i, j = 0, 0
        # start_list = list(start)
        n = len(start)
        while i < n or j < n:
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1
            
            if start[i] != target[j]: return False
            if start[i] == 'L':
                if i < j : 
                    return False

            if start[i] == 'R' and i > j: return False

            i += 1
            j += 1

        return True


       