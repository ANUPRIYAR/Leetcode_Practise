class Solution:
    def maxOperations(self, s: str) -> int:
        # traverse and find 1st index with 1 and next index with 0 and move it by 1 if next is 0, and replace current index by 0
        ones = 0
        max_moves = 0
        for i in range(len(s)): # 1001101
            # print(f"i at start: {i}")
            if s[i] == '1':
                # print("one found")   # i= 3
                ones += 1   
                # print(f"ones: {ones}")
            # elif i < len(s) - 1 and s[i] == '0' and s[i + 1] == '0':
            #     pass
                # print(f" double 0 found")
                
            elif (i < len(s) - 1 and s[i] == '0' and s[i +1] == '1' ) or (i==len(s)-1 and s[i] == '0'):
                # print(F"01 PAIR FOUND")
                max_moves += ones
                # print(f"max_moves updated :{max_moves} ones was:{ones}")

        # print(f"final max moves: {max_moves}")
        return max_moves

       