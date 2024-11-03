class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        str_len = len(s)
        goal_len = len(goal)

        if str_len != goal_len:
            return False

        
        for i in range(2* str_len):
            first_part = s[ : i% str_len]
            second_part = s[i % str_len:]
            print(first_part , second_part)
            if second_part + first_part == goal:
                return True
        return False

        # get starting position
        # while i < str_len and s[i:end] != goal[j:]:
        #     j += 1

        # print(j)


        # # match all characters
        # for i in range(str_len):
        #     if s[i] != goal[j % str_len]:
        #         return False
        #     j += 1

        # return True
        






        