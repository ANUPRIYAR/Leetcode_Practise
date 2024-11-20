class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # freq = dict()
        freq = {"a" : 0 , "b" : 0, "c":0}
        if k == 0:
            return 0
        left, right  = 0, len(s)- 1
        minutes = 0
        flag = False
        
        min_minutes = float("inf")
        n= len(s)
        limit = -1
        while limit <= len(s)//2 + 1:
            freq["a"],  freq["b"], freq["c"] = 0, 0, 0
            left, right = 0, len(s) - 1
            minutes = 0

            while left <= limit and left < len(s):
                freq[s[left]] += 1
                minutes += 1
                left += 1
            left = left - 1
            # print(f"left:{left}")
            while right > left and (freq["a"] < k or freq["b"] < k or freq["c"] < k):
                freq[s[right]] += 1
                minutes += 1
                right -= 1
            right = right + 1

            # print(f"right: {right}")
            # print(f"freq:{freq}")
            
            # minutes = left + len(s) - right 
            print(f"minutes:{minutes}")
            if freq["a"] >= k and freq["b"] >= k and freq["c"] >= k:
                min_minutes = min(min_minutes, minutes)
        
            limit += 1
            

        return min_minutes if min_minutes != float('inf') else -1

            







        